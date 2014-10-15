
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.scatterlayout import ScatterLayout
import random



class MyBigImage(FloatLayout):
    def __init__(self, **kwargs):
        super(MyBigImage, self).__init__(**kwargs)
	for i in range(20):
		self.addImage("bluerose.png")

    def addImage(self, filename):
        self.image = Image(source=filename, mipmap=True)
	self.image.size_hint = None, None
	self.image.width = 140
	self.image.height = 140
	self.image.pos = 300+random.randint(-200,200), 200+random.randint(-150,150)
	self.add_widget(self.image)




if __name__ == '__main__':

    from kivy.app import App
    class TestApp(App):

        def build(self):
            self.root = MyBigImage()
            return self.root

    app = TestApp()
    app.run()

