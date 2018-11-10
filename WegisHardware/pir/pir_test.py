import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40,GPIO.IN)

while True:
    input_state = GPIO.input(40)
    if input_state == True:
	print("Motion Detected")
	time.sleep(1)

    else:
	print("not detected")
	time.sleep(1)


#after detect 20s -> none

