import time
import picamera
import subprocess
import config #user edit

now = time.localtime()
s = "%04d_%02d_%02d_%02d:%02d:%02d"%(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
srec = raw_input("input num::")


name = s + ".h264"
name2 = s + ".mp4"

set = 0
start = 0
count = 0

camera = picamera.PiCamera()
camera.resolution = (640, 480)


while(1):
    if srec == '1':
	#1 = start recode
	print srec + " = start recode"
	if set == 0 and start == 0:
	    camera.start_recording("1.h264")
	    start = 1

     	srec = raw_input("input num::")
#	break

    elif srec == '0':
	#2 = end recode
	print srec + " = stop recode"
	if start == 1:
	    camera.stop_recording()
	    print "stop cam"
	    call = "MP4Box -add" + " " + "1.h264" + " " + name2
	    subprocess.call(call, shell=True)
	    subprocess.call("rm 1.h264 ",shell=True)
	    print "success mk mp4 " + str(count) + " sec file"
	    call2 = "php putdata.php 2 " + s + " 00:00:10 " + str(config.fail_work)
	    print call2
	    break;
	#srec = raw_input("input num::")
#	break
