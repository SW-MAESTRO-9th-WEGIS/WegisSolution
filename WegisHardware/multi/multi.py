from multiprocessing import Process, Queue

import time
import touch
import mkv
import RPi.GPIO as GPIO
import time
import defprt
import picamera
import subprocess


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

camera = picamera.PiCamera() # camera init



while True:
    #q = Queue()
    input_state = GPIO.input(40)
    if input_state == True:
	if check_time == 0:
	    now = time.localtime()
	    times = "%04d_%02d_%02d_%02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
#	    print time
	    check_time = 1
	    p3.start()
	    #print q.get()
	#print("Motion Detected")
	#time.sleep(1)

	if start_cam == 0:
	    start_cam = 1
	    print "detect human & start record "
	    name = times + ".mp4"
	    count += 1 # delete
	    camera.start_recording("1.h264") # make name
    else:
	#print("Detecting ... ...")
	check_time = 0
	#time.sleep(1)
	if start_cam == 1:
	    start_cam = 0
	    camera.stop_recording()
	    print " stop record "
	    call = "MP4Box -add "+"1.h264 "+ name
	    print call
	    subprocess.call(call, shell=True)
	    subprocess.call("rm 1.h264 ", shell=True)
	    print "success to make mp4 file"
	    #p3.exit()
	    # need php script & during time
	    #camera.close() => error!


#p3.join()

#after detect 20s -> none


#if __name__ == '__main__':


    #p1 = Process(target=func2, args=(0,))
    #time.sleep(5)
    #p1 = Process(target=func2, args=(1,))


    #p1.start()

    #p1.join()

