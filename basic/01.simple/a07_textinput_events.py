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
	self.textinput.bind(cursor_row=self.rowChanged)

    def rowChanged(self, instance, row):
	print "Current Row", row

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



"""
    :Events:
        `on_text_validate`
            Fired only in multiline=False mode when the user hits 'enter'.
            This will also unfocus the textinput.
        `on_double_tap`
            Fired when a double tap happens in the text input. The default
            behavior selects the text around the cursor position. More info at
            :meth:`on_double_tap`.
        `on_triple_tap`
            Fired when a triple tap happens in the text input. The default
            behavior selects the line around the cursor position. More info at
            :meth:`on_triple_tap`.
        `on_quad_touch`
            Fired when four fingers are touching the text input. The default
            behavior selects the whole text. More info at
            :meth:`on_quad_touch`.


"""
