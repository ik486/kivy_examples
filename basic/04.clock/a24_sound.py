
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.scatterlayout import ScatterLayout
import random
from kivy.clock import Clock
Clock.max_iteration = 20

from kivy.core.audio import SoundLoader



class MyBigImage(FloatLayout):
    def __init__(self, **kwargs):
        super(MyBigImage, self).__init__(**kwargs)
	self.velocity = [8, 6]
	self.addImage("bluerose.png")
	self.sound = self.sound = SoundLoader.load("glass.ogg")
	Clock.schedule_interval(self.moving, 1.0/3)

    def addImage(self, filename):
        self.image = Image(source=filename, mipmap=True)
	self.image.size_hint = None, None
	self.image.width = 140
	self.image.height = 140
	self.image.pos = 300+random.randint(-200,200), 200+random.randint(-150,150)
	self.add_widget(self.image)
	self.image.bind(on_touch_down=self.touchMove)


    def moving(self, dt):
	self.sound.play()
        x, y = self.image.pos
        if x < 0: x = 0
        if y < 0: y = 0
        x = x + self.velocity[0]
        y = y + self.velocity[1]
        self.image.pos = x, y
        ww = app.root.width - 128
        hh = app.root.height - 128
        if x > ww:
                self.velocity[0] = - random.randint(1,10)
	elif x <= 0:
                self.velocity[0] =  random.randint(1,10)
        if y > hh:
                self.velocity[1] = - random.randint(1,10)
	elif y <= 0:
                self.velocity[1] =  random.randint(1,10)
	return

    def touchMove(self, image, touch):
	if image.collide_point( *touch.pos):
		Clock.unschedule(self.moving)
		return True
        return super(MyBigImage, self).on_touch_down(touch)





if __name__ == '__main__':

    from kivy.app import App
    class TestApp(App):

        def build(self):
            self.root = MyBigImage()
            return self.root

    app = TestApp()
    app.run()

