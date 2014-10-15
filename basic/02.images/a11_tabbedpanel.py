from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem


from a09_gridlayout import MyGrid1
from a10_images import MyGrid2

class MyTab(TabbedPanel):
    def __init__(self, **kwargs):
        super(MyTab, self).__init__(**kwargs)
        self.do_default_tab = False
        self.tab_pos = 'left_top'
	self.grid1 = MyGrid1()
	self.tab1  = self.addTab("Data", self.grid1)
	self.grid2 = MyGrid2()
	self.tab2 = self.addTab("Images", self.grid2)
	self.set_def_tab(self.tab1)

	self.grid1.button2.bind(on_press=self.dataButton)
	self.grid2.button2.bind(on_press=self.imageButton)


    def addTab(self, name, obj):
    	th = TabbedPanelItem(text=name)
    	self.add_widget(th)
	th.add_widget(obj)
	th.background_down = "blue.jpeg"
	print dir(th)
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


