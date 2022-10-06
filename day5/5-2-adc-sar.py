import time
import RPi.GPIO as GPIO

dac = (26, 19, 13, 6, 5, 11, 9, 10)
comp = 4
troyka = 17
def decimal2binary(value): 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]
def adc():
    
    for i in range(0, 255):
            signal = decimal2binary(i)
            GPIO.output(dac, signal)
            
            time.sleep(0.001)
            
            comp_value = GPIO.input(4)
            if comp_value == 0:
                return i/(2**8)*3.3

GPIO.setmode(GPIO.BCM)
for count in range(0,8):
    GPIO.setup(dac[count], GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)



try:
    while(1):
        print (adc())

except KeyboardInterrupt:
    print('stop')
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()