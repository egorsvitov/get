import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

leds = (21, 20, 16, 12, 7, 8, 25, 24)

aux = (22, 23 ,27, 18, 15, 14, 3, 2)

for count in range(0,8):
    GPIO.setup(leds[count], GPIO.OUT)

for count in range(0,8):
    GPIO.setup(aux[count], GPIO.IN)
while(1):
    for count in range(0, 8):
        GPIO.output(leds[count], GPIO.input(aux[count]))
