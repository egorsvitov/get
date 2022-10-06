import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = (21, 20, 16, 12, 7, 8, 25, 24)

for count in range(0,3):
    for count in range(0,8):
        GPIO.setup(leds[count], GPIO.OUT)
        GPIO.output(leds[count], 1)
        time.sleep(0.2)
        GPIO.output(leds[count], 0)
GPIO.cleanup()