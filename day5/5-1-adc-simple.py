import RPi.GPIO as GPIO
import time

dac = (26, 19, 13, 6, 5, 11, 9, 10)
comp = 4
troyka = 17

def decimal2binary(value): 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]
def adc():
    inp = 0
    GPIO.output(troyka, 1)
    for i in range(7, -1, -1):
        GPIO.output(dac, decimal2binary(inp + 2**(i)))
        time.sleep(0.001)
        if GPIO.input(comp) == 1:
            inp += 2**(i)
    return((inp*3.3/(2**8)))

GPIO.setmode(GPIO.BCM)
for count in range(0,8):
    GPIO.setup(dac[count], GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = 0)
GPIO.setup(comp, GPIO.IN)

try:
    while(1):
        print(adc())

except KeyboardInterrupt:
    print('stop')
finally:
    GPIO.output(dac, 0)
    GPIO.output(17, 0)
    GPIO.cleanup()