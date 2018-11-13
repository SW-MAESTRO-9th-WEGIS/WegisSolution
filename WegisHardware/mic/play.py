import subprocess


subprocess.call("arecord -D plughw:1,0 -d 30 ks2.wav" ,shell=True)
