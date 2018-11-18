from multiprocessing import Process, Queue

import time
import touch
import RPi.GPIO as GPIO
import eyes
import picamera
import subprocess
import os
import cv2
import numpy as np

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40,GPIO.IN)

def func1():
    pass
    '''global fail_work
    print ("a")
    time.sleep(1)
    fail_work = touch.touch()
    print "fail count : "+str(fail_work)'''

def func2(x):
    mkv.make_video(x)

def func3():
    touch.touch()

#    defprt.defprt()

#q = Queue()
p3 = Process(target=func3)  #, args=(q,)) # call p3

start_cam = 0 # start switch
check_time = 0 #for save time
count = 0 # delete

#camera = picamera.PiCamera() # camera init
cap = cv2.VideoCapture(0)

p3.start()

while True:
    #q = Queue()
    input_state = GPIO.input(40)
    if input_state == True:
	count += 1
	time.sleep(1)
	if check_time == 0:
	    now = time.localtime()
	    times = "%04d-%02d-%02d_%02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
	    t = open("time.txt", 'w')
	    t.write(times)
	    t.close()
#	    print time
	    check_time = 1

	if start_cam == 0:
	    start_cam = 1
	    print "detect human & start record "
	    name = times + ".mp4"
	    count = 1 # delete
	    #camera.start_recording("1.h264") # make name
	    out = cv2.VideoWriter(name,0x00000021,20.0,(640,480))
	else :
	    ret, frame = cap.read()
	    out.write(frame)
	    print "write"
    else:
	#print("Detecting ... ...")
	check_time = 0
	#time.sleep(1)
	if start_cam == 1:
	    start_cam = 0
	    #camera.stop_recording()
	    out.release()
	    print " stop record "
	    #call = "MP4Box -add "+"1.h264 "+ name
	    d_sec = "%02d" % (count%60)
	    d_min = "%02d" % (count/60)
	    dd_min = (count/60)
	    d_hour = "%02d" % (dd_min/60)
	    during = str(d_hour)+":"+str(d_min)+":"+str(d_sec)
	    php_call = "php putdata.php 2 "+ name + " " + times + " " + str(during)
	    #print call
	    print php_call
	    #subprocess.call(call, shell=True)
	    time.sleep(1)
