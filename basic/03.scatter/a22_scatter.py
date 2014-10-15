from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.scatterlayout import ScatterLayout



class MyBigImage(FloatLayout):
    def __init__(self, **kwargs):
        super(MyBigImage, self).__init__(**kwargs)
	self.addImage("oak.jpeg")

    def addImage(self, filename):
	self.layout = ScatterLayout()
        #self.layout.scale = 1.8
        #self.layout.scale_min= 1.5
        #self.layout.scale_max= 4.5
        self.image = Image(source=filename, mipmap=True)
	self.layout.add_widget(self.image)
	self.add_widget(self.layout)



if __name__ == '__main__':

    from kivy.app import App
    class TestApp(App):

        def build(self):
            self.root = MyBigImage()
            return self.root

    app = TestApp()
    app.run()

