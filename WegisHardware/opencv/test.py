import numpy as np
import cv2
import RPi.GPIO as GPIO
import picamera
import subprocess

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40,GPIO.IN)
#cap = cv2.VideoCapture(0)


#cap = cv2.VideoCapture(0)   #defining the webcam
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('webcamOut.avi',fourcc,30.0,(640,480))
stat = 0
#first = 0
name = 0
#camera = picamera.PiCamera()
cap = cv2.VideoCapture(0)
while True:
    input_state = GPIO.input(40)
    if input_state == True:
	if stat == 0 :
	    #cap = cv2.VideoCapture(0)   #defining the webcam
	    #cap.open(0)
	    fourcc = cv2.VideoWriter_fourcc(*'XVID')
	    name = name + 1
	    named = str(name)+".avi"
	    out = cv2.VideoWriter(named,fourcc,30.0,(640,480))
	    stat = 1
	else :
    	    ret, frame = cap.read()
    	    out.write(frame)
    	    cv2.imshow('frame',frame)
    	if cv2.waitKey(1) & 0xFF ==ord('q'):
            break

    else :
	if stat == 1:
#	    cap.close(0)
	    out.release()
	    #cap.release()
	    cv2.destroyAllWindows()
	    stat = 0
#	    camera.close()
	    #subprocess.call("sudo python test.py", shell=True)
	else :
	    pass


cap.release()
