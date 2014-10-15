from kivy.uix.scrollview import ScrollView

from a14_grid_fixedsize import MyGrid1

class MyScroll(ScrollView):
    def __init__(self, **kwargs):
        super(MyScroll, self).__init__(**kwargs)
	self.grid1 = MyGrid1()
	self.add_widget(self.grid1)
	self.grid1.size_hint_y = None
	self.grid1.bind(minimum_height=self.grid1.setter("height"))
	return 


if __name__ == '__main__':

    from kivy.app import App
    class TestApp(App):

        def build(self):
            self.root = MyScroll()
            return self.root

    app = TestApp()
    app.run()

