import threading
import time


class MyThread(threading.Thread):
        def __init__(self, t, *args):
                threading.Thread.__init__(self, target=t, args=args)
                self.start()


def myfunction_one(a, b, c):
	time.sleep(3)
	print a, b, c



print "Hello CUSAT"

MyThread(myfunction_one, 34, 56, 78)

print "Bye CUSAT"
