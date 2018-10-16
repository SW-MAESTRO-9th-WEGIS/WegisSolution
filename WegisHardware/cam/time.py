import picamera
import time

now = time.localtime()

s = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

print s

name = s + ".h264"

print name

camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.start_recording("1.h264") # name...
camera.wait_recording(3)
camera.stop_recording()
