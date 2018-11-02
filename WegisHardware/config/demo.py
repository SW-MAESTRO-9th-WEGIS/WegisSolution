import RPi.GPIO as GPIO
import time
import subprocess

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40,GPIO.IN)


count = 0
while True:
    if count == 0:
	now = time.localtime()
	s = "%04d.%02d.%02d_%02d:%02d:%02d"%(now.tm_year,now.tm_mon,now.tm_mday,now.tm_hour, now.tm_min, now.tm_sec)

    input_state = GPIO.input(40)
    if input_state == True:
        print("Motion Detected")
        time.sleep(1)
	count = count + 1

    else:
        print("not detected")
	if count > 0:
	    name = "touch " + s + "__" + str(count) + "sec" + ".txt"
	    subprocess.call(name,shell=True)
	    print("Make Report")
	    count = 0
	else:
            time.sleep(1)
    	    count = 0

