import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
def decimal2binary(value):
 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]
dac = (26, 19, 13, 6, 5, 11, 9, 10)
for count in dac:
    GPIO.setup(count, GPIO.OUT) 
inp_number = 0
try:
    while(-1 < inp_number < 256):
        inp_number = (int(input()))
        print("напряжение:", 3.3*inp_number/255)
        number_bin = decimal2binary((inp_number))
        for count in range(0,8):
            if number_bin[count] == 1:
                GPIO.output(dac[count], 1)
            else:
                GPIO.output(dac[count], 0)
except:
    print("quit")
finally:
    for count in range(0,8):
        GPIO.output(dac[count], 0)