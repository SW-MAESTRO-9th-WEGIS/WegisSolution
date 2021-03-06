def eyes():
    #to create timelapse videos from still you need to: sudo apt-get install libav-tools
    #to playback the video using mplayer you need to : sudo apt-get install mplayer
    import os
    import numpy as np
    import cv2
    import datetime
    import imutils
    import time
    import subprocess

    # need opencv  library
    # sudo pip3 install imutils
    # " sudo python3 mogmog.py "

    cap = cv2.VideoCapture(0)
    #codec = cv2.VideoWriter_fourcc(*'X264')

    out = cv2.VideoWriter('test.mp4', 0x00000021, 20.0, (320,240))

    #cap = cv2.resize(capp, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
    fgbg = cv2.createBackgroundSubtractorMOG2(varThreshold=150)
    #carsPerSecond = 0
    eachCar = 0
    oldX = 0
    oldY = 0
    oldSec = 0
    totalCarsSeen = 0
    start = time.time()
    runSince = time.strftime("%H:%M:%S")

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

    while(1):
        ret, frame = cap.read()
        #out.write(frame)

        count = cap.get(cv2.CAP_PROP_POS_FRAMES)
    # left = '1.bmp'
    # left = cv2.imread(left) #, cv2.IMREAD_GRAYSCALE)
    # left = cv2.resize(left, (800,480))

        show = mid
    #    warning = 'warning.png'
    #    warning = cv2.imread(warning, cv2.IMREAD_GRAYSCALE)
    #    mid = cv2.resize(mid, (100,80))
        if int(count)%1 == 0:
            frame = cv2.resize(frame, (320, 240))
            out.write(frame)
    ##
    #        kernel = np.ones((2,2), np.float32)/4 # / k*2
    #        frame = cv2.filter2D(frame, -1, kernel)
    ##
            fgmask = fgbg.apply(frame)
    #        fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
            kernel2 = np.ones((5,5),np.uint8)
            erosion = cv2.erode(fgmask,kernel2,iterations = 2)
            dilation = cv2.dilate(erosion,kernel2,iterations = 2)
    #        cv2.rectangle(frame, (80, 25), (250, 100), (0, 255, 0), 2) # DEBUG Displays co-ordinates and size of countours detected

            im2, contours, hierarchy = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
            for c in contours:
            # if the contour is too small, ignore it
                if cv2.contourArea(c) < 500:
                    continue

        # compute the bounding box for the contour, draw it on the frame,
        # and update the text
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #            print("x=", x, "y=", y, "width=", w, "height=", h) #DEBUG line: Displays co-ordinates and size of countours detected

                #if y < 30 and w > 50 and w < 200 and h > 200:
                #    timestr = time.strftime("%S")
                #print("timestr=" + str(timestr) + "oldSec=" + str(oldSec)) #Debug line
                #    if timestr == oldSec or int(timestr) == int(oldSec) + 1:
                #        end = time.time()
                #        elapsed = end - start
                #        if elapsed > 10:
                #            totalCarsSeen += 1
                #            print("------------------------------------------")
                #            print("Total Human Seen Since " + str(runSince) + " = " + str(totalCarsSeen))
                #            print("------------------------------------------")
                #            oldX = 0
                #            oldY = 0
                        #cv2.imwrite('car{0:04d}.png'.format(totalCarsSeen), frame) # only saves one frame for each car, moved it.

                #        fulltimestr = time.strftime("%H:%M:%S")
                #        print("Detect Human " + fulltimestr)
    #               cv2.imwrite('car{0:04d}.png'.format(eachCar), frame) # this saves each car frame to a PNG file and numbers them sequantially.
                #        eachCar += 1
                #        if oldX != 0 and oldX > x:
                #            print("going left")
                #        if oldX != 0 and oldX < x:
                #            print("going right")
                #        oldX = x
                #        oldY = y
                #        start = time.time()

                #    oldSec = timestr
    #            if x > 475 and h > 100:
    #                print("Intruders")
                #    timestrI = time.strftime("%Y%m%d-%H%M%S")
    #            cv2.imwrite('intruder' + timestrI + '.png', frame)
        if w < 120:
            if x < 108:
    #		subprocess.call("cat left.txt", shell=True)
                show = left
#                print "left"
            elif x < 216:
    #		subprocess.call("cat mid.txt", shell=True)
                show = mid
#                print "middle"
            elif x < 320:
    #		subprocess.call("cat right.txt", shell=True)
                show = right
#                print "right"
        else:
    #	    show = warning
            pass #	    print "Too close ... Warning !!"
    #        cv2.imshow('Background Subtractor MOG2',fgmask)
    #        cv2.imshow("Security Feed", frame)
            cv2.namedWindow("change", cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty("change",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
            cv2.imshow("change", show)
    #       cv2.imshow("Erosion", erosion)
    #      cv2.imshow("Dilation", dilation)
        
        
        # You have to click on a Video Window for the control keys to work, not the terminal window
        key=cv2.waitKey(30) & 0xFF
        # Press c to create a timelapse video - you need libav-tools installed 
    #        if key == 99:
    #            print("Creating timelapse video")
    #            os.system("rm cartimelapse.mp4")
    #            os.system("avconv -r 10 -i car%04d.png -r 10 -vcodec libx264 -vf scale=640:480 cartimelapse.mp4 &")
    #            os.system("clear")
        # Press p to playback the timelapse video - you need mplayer installed
    #        elif key == 112:
    #            print("Play timelapse video")
    #            os.system("mplayer cartimelapse.mp4 &")
    #            os.system("clear")
        # Press ESC to Exit
        if key  == 27:
            break
            
        else:
            pass
    cap.release()
    out.release()
    cv2.destroyAllWindows()
