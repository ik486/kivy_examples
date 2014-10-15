from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy import metrics


class MyGrid1(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid1, self).__init__(**kwargs)
	self.cols = 2
	self.fields = []
	self.addField("First Name")
	self.addField("Middle Name")
	self.addField("Last Name")
	self.addField("Age")
	self.addField("Qualification")
	self.addField("Designation")
	self.addField("House Name")
	self.addField("Address")
	self.addField("Street")
	self.addField("City")
	self.addField("District")
	self.addField("State")
	self.button1 = Button(text="Save", size_hint_y=None, height=metrics.sp(80))
	self.button2 = Button(text="Next", size_hint_y=None, height=metrics.sp(80))
	self.add_widget(self.button1)
	self.add_widget(self.button2)
        self.button1.bind(on_press=self.savePressed)

    def addField(self, name):
	text_label = Label(text=name)
	text_input = TextInput(multiline=False)
	text_label.size_hint_y = None
	text_input.size_hint_y = None
	text_label.height = metrics.sp(80)
	text_input.height = metrics.sp(80)
	self.add_widget(text_label)
	self.add_widget(text_input)
	self.fields.append([text_label, text_input])
	return

    def savePressed(self, instance):
	for label, textinput in self.fields:
		print "%20s : %s" % (label.text, textinput.text)


if __name__ == '__main__':

    from kivy.app import App
    class TestApp(App):

        def build(self):
            self.root = MyGrid1()
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
