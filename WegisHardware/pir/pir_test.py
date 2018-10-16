import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.IN)

while True:
    input_state = GPIO.input(21)
    if input_state == True:
	print("Motion Detected")
	time.sleep(2)
