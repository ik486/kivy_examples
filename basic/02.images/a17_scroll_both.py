from kivy.uix.scrollview import ScrollView

from a16_images_fixedsize import MyGrid2

class MyScroll(ScrollView):
    def __init__(self, **kwargs):
        super(MyScroll, self).__init__(**kwargs)
	self.grid1 = MyGrid2()
	self.add_widget(self.grid1)
	self.grid1.size_hint = None, None
	self.grid1.bind(minimum_height=self.grid1.setter("height"))
	self.grid1.bind(minimum_width=self.grid1.setter("width"))
	return 


if __name__ == '__main__':

    from kivy.app import App
    class TestApp(App):

        def build(self):
            self.root = MyScroll()
            return self.root

    app = TestApp()
    app.run()

