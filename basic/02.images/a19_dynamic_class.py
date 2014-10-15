from kivy.uix.scrollview import ScrollView

from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy import metrics



class MyScroll(ScrollView):
    def __init__(self, **kwargs):
        super(MyScroll, self).__init__(**kwargs)
	self.grid1 = GridLayout(cols=10)
	self.add_widget(self.grid1)
	self.grid1.size_hint = None, None
	self.grid1.bind(minimum_height=self.grid1.setter("height"))
	self.grid1.bind(minimum_width=self.grid1.setter("width"))
	for i in range(20):
		for j in range(10):
			ti = TextInput(size_hint=(None, None))
			ti.width = metrics.sp(160)
			ti.height = metrics.sp(40)
			if i > 2:
				ti.row = i
				ti.col = j
			self.grid1.add_widget(ti)
			ti.bind(text=self.textChanged)
	return 


    def textChanged(self, instance, val):
	if getattr(instance, "row", None):
		print instance.row, instance.col, val
	else:
		print "Variable row is not implimented"


if __name__ == '__main__':

    from kivy.app import App
    class TestApp(App):

        def build(self):
            self.root = MyScroll()
            return self.root

    app = TestApp()
    app.run()

