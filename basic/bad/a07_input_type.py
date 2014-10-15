from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


class MyBox(BoxLayout):
    def __init__(self, **kwargs):
        super(MyBox, self).__init__(**kwargs)
	self.orientation = "vertical"
	self.button1 = Button(text="Hello")
	self.textinput = TextInput()
	self.textinput.size_hint_y = 0.9
	self.button1.size_hint_y = 0.1
	self.button1.bind(on_press=self.mypress)
	self.button1.bind(on_release=self.myrelease)
	self.textinput.bind(text=self.myText)
	self.add_widget(self.button1)
	self.add_widget(self.textinput)
	self.textinput.input_type = 'number'
	#text, number, url, mail, datetime, tel, address.

    def mypress(self, button):
	print button.text, "Pressed"

    def myrelease(self, button):
	print button.text, "Released"

    def myText(self, instance, value):
	print value, "TEXT CHANGED"


if __name__ == '__main__':

    from kivy.app import App
    class TestApp(App):

        def build(self):
            self.root = MyBox()
            return self.root

    app = TestApp()
    app.run()

