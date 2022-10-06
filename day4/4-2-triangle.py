import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
def decimal2binary(value):
 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]
dac = (26, 19, 13, 6, 5, 11, 9, 10)
period = int(input("период (с):"))
for count in dac:
    GPIO.setup(count, GPIO.OUT)
    GPIO.output(dac[count], 1)
try: 
    while(1):
        for number in range(0,255):
            number_bin = decimal2binary(number)
            time.sleep(period/512)
            for count in range(0,8):
                if number_bin[count] == 1:
                    GPIO.output(dac[count], 1)
                else:
                    GPIO.output(dac[count], 0)
        for number in range(255,0,-1):
            number_bin = decimal2binary(number)
            time.sleep(period/512)
            for count in range(0,8):
                if number_bin[count] == 1:
                    GPIO.output(dac[count], 1)
                else:
                    GPIO.output(dac[count], 0)
except KeyboardInterrupt:
    for count in range(0,8):
        GPIO.output(dac[count], 0)