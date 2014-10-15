import threading
import time


class MyThread(threading.Thread):
        def __init__(self, t, *args):
                threading.Thread.__init__(self, target=t, args=args)
                self.start()



class MyTestClass:
	def __init__(self):
		self.c = 0
		return

	def yourfunction(self, a, b):
		time.sleep(2)
		self.c = a*b
		self.display()

	def display(self):
		print self.c




obj = MyTestClass()

print "Hello CUSAT"

MyThread(obj.yourfunction, 34, 56)

print "Bye CUSAT"
