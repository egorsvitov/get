import time
import RPi.GPIO as GPIO
import matplotlib.pyplot as plt

dac = (26, 19, 13, 6, 5, 11, 9, 10)
leds = (24, 25, 8, 7, 12, 16, 20, 21)
comp = 4
troyka = 17
def decimal2binary(value): 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]
def adc():
    inp = 0
    for i in range(7, -1, -1):
        GPIO.output(dac, decimal2binary(inp + 2**(i)))
        time.sleep(0.001)
        if GPIO.input(comp) == 1:
            inp += 2**(i)
    return((inp*3.3/(2**8)))
def volume():
    voltage = adc()
    for count in range(0, 8):
        if count < voltage*8//3.3:
            GPIO.output(leds[count], 1)
        else:
            GPIO.output(leds[count], 0)
    reports_v.append(voltage)
    reports_t.append(time.time() - start)
    print (voltage)
    return voltage

GPIO.setmode(GPIO.BCM)
for count in range(0,8):
    GPIO.setup(leds[count], GPIO.OUT)
    GPIO.setup(dac[count], GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT)
GPIO.output(troyka, 1)
GPIO.setup(comp, GPIO.IN)
reports_v = []
reports_t = []

for count in range(0, 8):
            GPIO.output(leds[count], 0)
try:
    start = time.time()
    while(volume() < 3):
        volume()
    GPIO.output(troyka, 0)
    while(volume() > 0.3):
        volume()
    finish = time.time()
    plt.scatter(reports_t, reports_v)
    plt.show()
except KeyboardInterrupt:
    print('stop')
    plt.scatter(reports_t, reports_v)
    plt.show()
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()