import RPi.GPIO as GPIO
import time

dac = (26, 19, 13, 6, 5, 11, 9, 10)
comp = 4
troyka = 17
def decimal2binary(value): 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]
def adc(value):
    signal = decimal2binary(value)
    GPIO.output(dac, signal)
    return signal

GPIO.setmode(GPIO.BCM)
for count in range(0,8):
    GPIO.setup(dac[count], GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)

try:
    while(1):
        inp = 0
        for i in range(8,0, -i):
            time.sleep(0.01)
            x = adc(inp + 2 ** i)
            if GPIO.input(4) == 0:
                inp = inp + 2**i
            #print (inp)
            #signal = adc(inp)
        voltage = inp/(2**8)*3.3
        print(voltage)

except KeyboardInterrupt:
    print('stop')
else:
    print('asd')
finally:
    GPIO.output(dac, 0)
    GPIO.output(4, 0)
    GPIO.cleanup(dac)