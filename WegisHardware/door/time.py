#f = open("time.txt",'w')

#data = 1

#f.write(str(data))
#f.close()


f = open("time.txt",'r')

while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()
