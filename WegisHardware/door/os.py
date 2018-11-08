import os
import subprocess
import time
#subprocess.call("echo $now_time", shell=True)
#for item in os.environ:
#    print("%s = %s"%(item, os.environ[item]))

#if ("kkk" in os.environ == True):
#    print "kkkk"

#subprocess.call("export rrr=1", shell=True)

#else:
#    print "ffff"
#print s

os.environ['rrr'] = "11"

subprocess.call("export",shell=True)

#time.sleep(30)

s = os.environ.get('kkk')
print s
#print keys

