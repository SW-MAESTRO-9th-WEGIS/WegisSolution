import picamera
import time
import subprocess

now = time.localtime()

s = "%04d.%02d.%02d_%02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
#now.tm_year
print s

name = s + ".h264"
name2 = s + ".mp4"

print name

camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.start_recording("1.h264") # name...
camera.wait_recording(3)
camera.stop_recording()

call = "MP4Box -add" + " " + name + " " + name2
print call
call2 = "MP4Box -add" + " " + "1.h264" + " " + name2
subprocess.call(call2, shell=True)
subprocess.call("rm 1.h264 ",shell=True)
