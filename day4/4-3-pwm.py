import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
#dac = (10, 9, 11, 5, 6, 13, 19, 26)

#GPIO.output(14, 1)
p = GPIO.PWM(3, 1000)
p.start(50)
while(1):
    a = int(input())   # use raw_input for Python 2
    p.ChangeDutyCycle(a)
input("dasd")
p.stop()
GPIO.cleanup()