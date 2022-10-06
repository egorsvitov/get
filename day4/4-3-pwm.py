import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.OUT)

p = GPIO.PWM(3, 1000)
p.start(50)

try:
    while(1):
        inp = int(input())
        print(3.3*inp/100)
        p.start(inp)
        
except KeyboardInterrupt:
    print("stop")
finally:
    p.start(0)
    GPIO.output(3, 0)
    GPIO.cleanup()