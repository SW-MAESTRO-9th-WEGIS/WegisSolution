from multiprocessing import Process
import time
import touch
import mkv

def func1():
    pass
    '''global fail_work
    print ("a")
    time.sleep(1)
    fail_work = touch.touch()
    print "fail count : "+str(fail_work)'''

def func2(x):
    mkv.make_video(x)


def func3():
    print ("c")


if __name__ == '__main__':


    p1 = Process(target=func2, args=(0,))
    time.sleep(5)
    p1 = Process(target=func2, args=(1,))


    p1.start()

    p1.join()

