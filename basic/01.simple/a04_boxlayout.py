from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class MyBox(BoxLayout):
    def __init__(self, **kwargs):
        super(MyBox, self).__init__(**kwargs)
	self.orientation = "vertical"
	self.button1 = Button(text="Hello")
	self.button2 = Button(text="Word")
	self.button1.bind(on_press=self.mypress)
	self.button1.bind(on_release=self.myrelease)
	self.button2.bind(on_press=self.mypress)
	self.button2.bind(on_release=self.myrelease)
	self.add_widget(self.button1)
	self.add_widget(self.button2)

    def mypress(self, button):
	print button.text, "Pressed"

    def myrelease(self, button):
	print button.text, "Released"



if __name__ == '__main__':

    from kivy.app import App
    class TestApp(App):

        def build(self):
            self.root = MyBox()
            return self.root

    app = TestApp()
    app.run()

