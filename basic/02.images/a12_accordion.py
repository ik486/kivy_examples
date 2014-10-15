from kivy.uix.accordion import Accordion, AccordionItem


from a09_gridlayout import MyGrid1
from a10_images import MyGrid2

class MyTab(Accordion):
    def __init__(self, **kwargs):
        super(MyTab, self).__init__(**kwargs)
	self.grid1 = MyGrid1()
	self.tab1  = self.addTab("Data", self.grid1)
	self.grid2 = MyGrid2()
	self.tab2 = self.addTab("Images", self.grid2)

	self.grid1.button2.bind(on_press=self.dataButton)
	self.grid2.button2.bind(on_press=self.imageButton)


    def addTab(self, name, obj):
    	th = AccordionItem(title=name)
    	self.add_widget(th)
	th.add_widget(obj)
	return th

    def dataButton(self, button):
	print "Next Button of Data Entry Form Pressed"

    def imageButton(self, button):
	print "Next Button of Display Images Pressed"

if __name__ == '__main__':

    from kivy.app import App
    class TestApp(App):

        def build(self):
            self.root = MyTab()
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
