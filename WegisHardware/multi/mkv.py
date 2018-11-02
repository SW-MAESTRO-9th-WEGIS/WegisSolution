def make_video(start):

    if start == 0:
        import time
        import picamera
        import subprocess
         #user edit

        now = time.localtime()
        s = "%04d_%02d_%02d_%02d:%02d:%02d"%(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

        name = s + ".h264"
        name2 = s + ".mp4"

        count = 0

        camera = picamera.PiCamera()
        camera.resolution = (640, 480)
        print "start recoding"
        camera.start_recording("1.h264")

#	break
#2 = end recode
    elif start == 1:
        camera.stop_recording()
	camera.close()
        print "stop cam"
        call = "MP4Box -add" + " " + "1.h264" + " " + name2
        subprocess.call(call, shell=True)
        subprocess.call("rm 1.h264 ",shell=True)
        print "success mk mp4 " + str(count) + " sec file"
        call2 = "php putdata.php 2 " + s + " 00:00:10 " + str(1)
        print call2
        
	#srec = raw_input("input num::")
#	break
