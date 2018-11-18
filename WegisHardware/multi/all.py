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
import imutils

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

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
fgbg = cv2.createBackgroundSubtractorMOG2(varThreshold=150)

i = 0

left = '../eyes/1.bmp'
left = cv2.imread(left)
left = cv2.resize(left, (800,480))

right = '../eyes/7.bmp'
right = cv2.imread(right)
right = cv2.resize(right, (800,480))

mid = '../eyes/4.bmp'
mid = cv2.imread(mid)
mid = cv2.resize(mid, (800,480))
show = mid

p3.start()

while True:
    #q = Queue()
    cv2.imshow("dddd",mid)
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
	    fgmask = fgbg.apply(frame)
	    kernel2 = np.ones((5,5),np.uint8)
            erosion = cv2.erode(fgmask,kernel2,iterations = 2)
            dilation = cv2.dilate(erosion,kernel2,iterations = 2)
	    im2, contours, hierarchy = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 

            for c in contours:
	        if cv2.contourArea(c) < 500:
            	    continue
		(x, y, w, h) = cv2.boundingRect(c)
            	cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
	    if w < 120:
	        if x < 108:
#		subprocess.call("cat left.txt", shell=True)
		    show = left
		    print "left"
	    	elif x < 216:
#		subprocess.call("cat mid.txt", shell=True)
		    show = mid
		    print "middle"
	    	elif x < 320:
#		subprocess.call("cat right.txt", shell=True)
		    show = right
		    print "right"
	    else :
		pass

#	    cv2.namedWindow("change", cv2.WND_PROP_FULLSCREEN)
#	    cv2.setWindowProperty("change",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
	    cv2.imshow("change", show)
	    print "write"
        key = cv2.waitKey(30) & 0xFF
	if key == 27:
	    break

	else:
	    pass
    else:
	#print("Detecting ... ...")
	check_time = 0
	#time.sleep(1)
	if start_cam == 1:
	    start_cam = 0
	    #camera.stop_recording()
	    out.release()
	    cv2.destroyAllWindows()
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
	    #subprocess.call(php_call, shell=True)
	    #subprocess.call("rm 1.h264 ", shell=True)
	    #print "success to make mp4 file"
	    #p3.exit()
	    # need php script & during time
	    #camera.close() => error!

cap.release()
#cv2.destroyAllWindows()
#p3.join()

#after detect 20s -> none


#if __name__ == '__main__':


    #p1 = Process(target=func2, args=(0,))
    #time.sleep(5)
    #p1 = Process(target=func2, args=(1,))


    #p1.start()

    #p1.join()

