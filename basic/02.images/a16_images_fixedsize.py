from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy import metrics


class MyGrid2(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid2, self).__init__(**kwargs)
	self.cols = 10
	self.fields = []
	self.button1 = Button(text="Save", size_hint=(None, None), width=metrics.sp(120), height=metrics.sp(120))
	self.button2 = Button(text="Next", size_hint=(None, None), width=metrics.sp(120), height=metrics.sp(120))
	self.add_widget(self.button1)
	self.add_widget(self.button2)
        self.button1.bind(on_press=self.savePressed)
	self.loadImages()

    def loadImages(self):
	import os
	files = os.listdir(".")
	for filename in files:
		if not filename.endswith(".png"): continue
		self.addImage(filename)

    def addImage(self, filename):
	image = Image(source=filename)
	image.size_hint = None, None
	image.width = metrics.sp(120)
	image.height = metrics.sp(120)
	self.add_widget(image)
	return

    def savePressed(self, instance):
	print "Save Pressed"


if __name__ == '__main__':

    from kivy.app import App
    class TestApp(App):

        def build(self):
            self.root = MyGrid2()
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
