#to create timelapse videos from still you need to: sudo apt-get install libav-tools
#to playback the video using mplayer you need to : sudo apt-get install mplayer
import os
import numpy as np
import cv2
import datetime
import imutils
import time

# need opencv  library
# sudo pip3 install imutils
# " sudo python3 mogmog.py "

cap = cv2.VideoCapture('video10.mp4')

#cap = cv2.resize(capp, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
fgbg = cv2.createBackgroundSubtractorMOG2()
#carsPerSecond = 0
eachCar = 0
oldX = 0
oldY = 0
oldSec = 0
totalCarsSeen = 0
start = time.time()
runSince = time.strftime("%H:%M:%S")

i = 0

while(1):
    ret, frame = cap.read()
    count = cap.get(cv2.CAP_PROP_POS_FRAMES)
    left = 'left.png'
    left = cv2.imread(left, cv2.IMREAD_GRAYSCALE)
    left = cv2.resize(left, (640,480))

    right = 'right.png'
    right = cv2.imread(right, cv2.IMREAD_GRAYSCALE)
    right = cv2.resize(right, (640,480))

    mid = 'mid.png'
    mid = cv2.imread(mid, cv2.IMREAD_GRAYSCALE)
    mid = cv2.resize(mid, (640,480))
    
    if int(count)%8 == 0:
        frame = cv2.resize(frame, (320, 240))
##
        kernel = np.ones((2,2), np.float32)/4 # / k*2
        frame = cv2.filter2D(frame, -1, kernel)
##
        fgmask = fgbg.apply(frame)
        fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
        kernel2 = np.ones((5,5),np.uint8)
        erosion = cv2.erode(fgmask,kernel2,iterations = 2)
        dilation = cv2.dilate(erosion,kernel2,iterations = 2)
    #cv2.rectangle(frame, (80, 25), (250, 100), (0, 255, 0), 2) # DEBUG Displays co-ordinates and size of countours detected

        im2, contours, hierarchy = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
        for c in contours:
        # if the contour is too small, ignore it
            if cv2.contourArea(c) < 500:
                continue

	# compute the bounding box for the contour, draw it on the frame,
	# and update the text
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        #print("x=", x, "y=", y, "width=", w, "height=", h) #DEBUG line: Displays co-ordinates and size of countours detected

            if y < 30 and w > 50 and w < 200 and h > 200:
                timestr = time.strftime("%S")
            #print("timestr=" + str(timestr) + "oldSec=" + str(oldSec)) #Debug line
                if timestr == oldSec or int(timestr) == int(oldSec) + 1:
                    end = time.time()
                    elapsed = end - start
                    if elapsed > 10:
                        totalCarsSeen += 1
                        print("------------------------------------------")
                        print("Total Human Seen Since " + str(runSince) + " = " + str(totalCarsSeen))
                        print("------------------------------------------")
                        oldX = 0
                        oldY = 0
                    #cv2.imwrite('car{0:04d}.png'.format(totalCarsSeen), frame) # only saves one frame for each car, moved it.

                    fulltimestr = time.strftime("%H:%M:%S")
                    print("Detect Human " + fulltimestr)
 #               cv2.imwrite('car{0:04d}.png'.format(eachCar), frame) # this saves each car frame to a PNG file and numbers them sequantially.
                    eachCar += 1
                    if oldX != 0 and oldX > x:
                        print("going left")
                    if oldX != 0 and oldX < x:
                        print("going right")
                    oldX = x
                    oldY = y
                    start = time.time()

                oldSec = timestr
            if x > 475 and h > 100:
                print("Intruders")
                timestrI = time.strftime("%Y%m%d-%H%M%S")
#            cv2.imwrite('intruder' + timestrI + '.png', frame)
	    if x < 108 :
		show = left
	    elif x < 216:
		show = mid
	    elif x < 320:
		show = right

#        cv2.imshow('Background Subtractor MOG2',fgmask)
        cv2.imshow("Security Feed", frame)
	cv2.imshow("change", show)
 #       cv2.imshow("Erosion", erosion)
  #      cv2.imshow("Dilation", dilation)
	
	
    # You have to click on a Video Window for the control keys to work, not the terminal window
        key=cv2.waitKey(30) & 0xFF
    # Press c to create a timelapse video - you need libav-tools installed 
        if key == 99:
            print("Creating timelapse video")
            os.system("rm cartimelapse.mp4")
            os.system("avconv -r 10 -i car%04d.png -r 10 -vcodec libx264 -vf scale=640:480 cartimelapse.mp4 &")
            os.system("clear")
    # Press p to playback the timelapse video - you need mplayer installed
        elif key == 112:
            print("Play timelapse video")
            os.system("mplayer cartimelapse.mp4 &")
            os.system("clear")
    # Press ESC to Exit
        elif key  == 27:
            break
        i=i+1
    
    else:
        pass
cap.release()
cv2.destroyAllWindows()
