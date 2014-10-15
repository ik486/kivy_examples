
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.scatterlayout import ScatterLayout
import random
from kivy.animation import Animation



class MyBigImage(FloatLayout):
    def __init__(self, **kwargs):
        super(MyBigImage, self).__init__(**kwargs)
	self.addImage("bluerose.png")

    def addImage(self, filename):
        self.button = Button()
        self.button.background_normal=filename
        self.button.background_down=filename
	self.button.size_hint = None, None
	self.button.border = [0,0,0,0]
	self.button.width = 140
	self.button.height = 140
	self.button.pos = 400, 350
	self.add_widget(self.button)
	self.button.bind(on_press=self.clicked)

    def clicked(self, button):
	animate1 = Animation(pos=(400, 100), t='in_elastic', duration=5)
	animate2 = Animation(pos=(400, 350), t='in_elastic', duration=5)
	animate3 = Animation(size=(250, 250), t='in_out_elastic', duration=5)
	animate4 = Animation(size=(140, 140), t='in_out_elastic', duration=5)
	a = (animate1 & animate3) + (animate2 & animate4)
	a.start(button)
	print "ok"




if __name__ == '__main__':

    from kivy.app import App
    class TestApp(App):

        def build(self):
            self.root = MyBigImage()
            return self.root

    app = TestApp()
    app.run()

