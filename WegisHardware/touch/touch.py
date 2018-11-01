#!/usr/bin/env python

import RPi.GPIO as GPIO
import mpr121
import time

# Use GPIO Interrupt Pin

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)

# Use mpr121 class for everything else

mpr121.TOU_THRESH = 0x30
mpr121.REL_THRESH = 0x33
mpr121.setup(0x5b)

# User pygame for sounds

# Track touches

touches = [0,0,0,0,0,0,0,0,0,0,0,0];
pwd = [0,0,0,0];
j = 0

while True:

    if (GPIO.input(7)): # Interupt pin is high
	pass
    else: # Interupt pin is low

	touchData = mpr121.readData(0x5b)

	for i in range(12):
	    if (touchData & (1<<i)):

		if (touches[i] == 0):

			print( 'Pin ' + (str(i+1)) + ' was just touched')
			time.sleep(0.3)
			touches[i] = 1;
			pwd[j] = (i+1)
			j=j+1
			if j==4 :
			    j=0

	    else:
		if (touches[i] == 1):
			print( 'Pin ' + str(i+1) + ' was just released')
			time.sleep(0.3)
			touches[i] = 0;
			print pwd
