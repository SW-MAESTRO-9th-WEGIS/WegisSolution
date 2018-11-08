import os
import time
import sys
 
#childs = {}
childs = {'$pa':'first child', '$pb':'second child'}
 
print "main start pid: %s" % (os.getpid())
 
for key in childs:
        newpid = os.fork()
 
        if newpid == 0:
                print "child %s" % (os.getpid())
                cnt = 1
                sleep_time = 1
                while True:
                        if cnt > 5:
                                print "child end"
                                break
                        print cnt
                        time.sleep(sleep_time)
                        cnt += 1
                sys.exit(0)
 
        else:
                childs[key] = newpid
                print "parent got newpid:%s" % (newpid)
 
for key in childs:
        print childs[key]
	print "kkk"
print "main end"
