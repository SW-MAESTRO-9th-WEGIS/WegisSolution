import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.IN)

try:
    while True:
	inputIO = GPIO.input(21)

	if inputIO == False:
		print "No input"
		time.sleep(0.5)

	else:
		print "!!!!!"
		time.sleep(0.5)

except KeyboardInterrupt:
	GPIO.cleanup()
