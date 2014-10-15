
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.scatterlayout import ScatterLayout
import random


class MyImage(Scatter):
    def __init__(self, no, **kwargs):
        super(MyImage, self).__init__(**kwargs)
	self.no = no
	self.image = Image(source="bluerose.png")
	self.add_widget(self.image)
	self.size_hint = None, None
	self.width = 140
	self.height = 140
	self.pos = 400-70+random.randint(-200,200), 300-70+random.randint(-150,150)

    def on_touch_down(self, touch):
	if self.image.collide_point( *touch.pos):
		print self.no
	else:
		print "failed", self.no
	return super(MyImage, self).on_touch_down(touch)


class MyBigImage(FloatLayout):
    def __init__(self, **kwargs):
        super(MyBigImage, self).__init__(**kwargs)
	for i in range(20):
		image = MyImage(i)
		self.add_widget(image)






if __name__ == '__main__':

    from kivy.app import App
    class TestApp(App):

        def build(self):
            self.root = MyBigImage()
            return self.root

    app = TestApp()
    app.run()

