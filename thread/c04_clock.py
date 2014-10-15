import threading
import time

from kivy.uix.button import Button
from kivy.clock import Clock



class MyThread(threading.Thread):
        def __init__(self, t, *args):
                threading.Thread.__init__(self, target=t, args=args)
                self.start()



class MyButton(Button):
	def __init__(self, **argv):
		super(MyButton, self).__init__(**argv)
		self.c = 0
		return

	def yourfunction(self, a, b):
		time.sleep(2)
		self.c = a*b
		trigger = Clock.create_trigger(self.mydisplay)
		trigger()

	def mydisplay(self, dt):
		print "OK"
		print self.c

	def on_press(self):
		print "Hello CUSAT"
		MyThread(self.yourfunction, 34, 56)
		print "Bye CUSAT"


if __name__ == '__main__':

    from kivy.app import App
    class TestApp(App):

        def build(self):
            self.root = MyButton(text='hello world')
            return self.root

    app = TestApp()
    app.run()

