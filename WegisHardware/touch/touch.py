#!/usr/bin/env python

import RPi.GPIO as GPIO
import mpr121
import time
import subprocess

# Use GPIO Interrupt Pin

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)

# Use mpr121 class for everything else

mpr121.TOU_THRESH = 0x30
mpr121.REL_THRESH = 0x33
mpr121.setup(0x5b)

# User pygame for sounds

# Track touches

touches = [0,0,0,0,0,0,0,0,0,0,0,0]; # 1~# button use
pass_pwd = [1,2,3,4]; # setting pwd
pwd = [0,0,0,0]; # pwd temp input
j = 0 # index
key = 0 # strlen(pwd) => door open
fail_work = 0

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

			if pass_pwd[j] == pwd[j]:
			    key = key + 1

			j=j+1

			if j==4 :
			    j=0
			    if key == 4:
				print "-------motor O"
				key = 0
			    else:
				print "-------motor X"
				key = 0
				fail_work = fail_work + 1
				fail_call = "php putdata.php 2 "+"time "+str(fail_work)
				print fail_call

	    else:
		if (touches[i] == 1):
			print( 'Pin ' + str(i+1) + ' was just released')
			time.sleep(0.3)
			touches[i] = 0;
			print pwd
			print key

