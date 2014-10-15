from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


class MyBox(BoxLayout):
    def __init__(self, **kwargs):
        super(MyBox, self).__init__(**kwargs)
	self.orientation = "vertical"
	self.button1 = Button(text="Hello")
	self.textinput1 = TextInput(multiline=False)
	self.textinput2 = TextInput(multiline=False)
	self.textinput3 = TextInput(multiline=False)
	self.add_widget(self.button1)
	self.add_widget(self.textinput1)
	self.add_widget(self.textinput2)
	self.add_widget(self.textinput3)
        self.textinput1.bind(on_text_validate=self.enterPressed)
        self.textinput2.bind(on_text_validate=self.enterPressed)
        self.textinput3.bind(on_text_validate=self.enterPressed)

    def enterPressed(self, instance):
	if instance == self.textinput1:
		self.textinput2.focus = True
	elif instance == self.textinput2:
		self.textinput3.focus = True
	elif instance == self.textinput3:
		self.textinput1.focus = True


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
