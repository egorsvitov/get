import time
import RPi.GPIO as GPIO

dac = (26, 19, 13, 6, 5, 11, 9, 10)
leds = (24, 25, 8, 7, 12, 16, 20, 21)
comp = 4
troyka = 17
def decimal2binary(value): 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]
def adc(value):
    signal = decimal2binary(value)

    GPIO.output(dac, signal)
    return signal
def volume():
    level = 0
    for i in range(0, 255):
        signal = adc(i)
        time.sleep(0.001)
        voltage = i/(2**8)*3.3
        comp_value = GPIO.input(4)
        if comp_value == 0:
            print(i)
            for count in range(0, 8):
                if count < i//32:
                    GPIO.output(leds[count], 1)
                else:
                    GPIO.output(leds[count], 0)
            break

GPIO.setmode(GPIO.BCM)
for count in range(0,8):
    GPIO.setup(leds[count], GPIO.OUT)
    GPIO.setup(dac[count], GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)


for count in range(0, 8):
            GPIO.output(leds[count], 0)
try:
    while(1):
        volume()
except KeyboardInterrupt:
    print('stop')
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()