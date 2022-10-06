import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = (10, 9, 11, 5, 6, 13, 19, 26)

inp_number = int(input())

number = []
for count in range(0,8):
    number.append(inp_number % 2)
    inp_number //= 2

for count in range(0,8):
    GPIO.setup(dac[count], GPIO.OUT)

for count in range(0,8):
    if number[count] == 1:
        GPIO.output(dac[count], 1)
    else:
        GPIO.output(dac[count], 0)

time.sleep(10)

for count in range(0,8):
    GPIO.output(dac[count], 0)

GPIO.cleanup()