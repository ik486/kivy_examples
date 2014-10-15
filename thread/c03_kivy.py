import threading
import time

from kivy.properties import NumericProperty
from kivy.uix.widget import Widget


class MyThread(threading.Thread):
        def __init__(self, t, *args):
                threading.Thread.__init__(self, target=t, args=args)
                self.start()

class MyTestClass(Widget):
	c = NumericProperty(0)
	def __init__(self):
		self.bind(c=self.display)
		return

	def yourfunction(self, a, b):
		time.sleep(2)
		self.c = a*b

	def display(self, instance, value):
		print self.c



obj = MyTestClass()

print "Hello CUSAT"

MyThread(obj.yourfunction, 34, 56)

print "Bye CUSAT"


"""

['AliasProperty', 'BooleanProperty', 'BoundedNumericProperty', 'DictProperty', 'ListProperty', 'NUMERIC_FORMATS', 'NumericProperty', 'ObjectProperty', 'ObservableDict', 'ObservableList', 'ObservableReferenceList', 'OptionProperty', 'Property', 'PropertyStorage', 'ReferenceListProperty', 'StringProperty', 'VariableListProperty', '__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '__test__', 'dpi2px', 'ref', 'string_types']


"""
