import RPi.GPIO as GPIO
import time
import picamera
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.IN)
now = time.localtime()

i = 0
setup = 0

while True:
    input_state = GPIO.input(21)
    if input_state == True:
	print("Motion Detected")
	time.sleep(2)
	
	if setup == 0:
            s = "%04d_%02d_%02d_%02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
#now.tm_year

            name = s + ".h264"
            name2 = s + ".mp4"

    	    camera = picamera.PiCamera()
    	    camera.resolution = (640, 480)
    	    camera.start_recording("1.h264") # name...
	    setup = 1
        else:
	    i = 0
    else:
	i = i+1
	if i == 3:
	    camera.stop_recording()
	    call = "MP4Box -add" + " " + name + " " + name2
 	    print call
 	    call2 = "MP4Box -add" + " " + "1.h264" + " " + name2
  	    subprocess.call(call2, shell=True)
  	    subprocess.call("rm 1.h264 ",shell=True)
	    i = 0
	    
