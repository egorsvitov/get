import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.OUT)
GPIO.output(21, 1)
time.sleep(0.5)
GPIO.output(21, 0)

GPIO.setup(20, GPIO.OUT)
GPIO.output(20, 1)
time.sleep(0.5)
GPIO.output(20, 0)

GPIO.setup(16, GPIO.OUT)
GPIO.output(16, 1)
time.sleep(0.5)
GPIO.output(16, 0)

GPIO.setup(12, GPIO.OUT)
GPIO.output(12, 1)
time.sleep(0.5)
GPIO.output(12, 0)

GPIO.setup(7, GPIO.OUT)
GPIO.output(7, 1)
time.sleep(0.5)
GPIO.output(7, 0)

GPIO.setup(8, GPIO.OUT)
GPIO.output(8, 1)
time.sleep(0.5)
GPIO.output(8, 0)

GPIO.setup(25, GPIO.OUT)
GPIO.output(25, 1)
time.sleep(0.5)
GPIO.output(25, 0)

GPIO.setup(24, GPIO.OUT)
GPIO.output(24, 1)
time.sleep(0.5)
GPIO.output(24, 0)
