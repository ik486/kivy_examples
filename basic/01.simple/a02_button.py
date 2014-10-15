from kivy.uix.button import Button


class MyButton(Button):
    def __init__(self, **kwargs):
        super(MyButton, self).__init__(**kwargs)
	self.bind(on_press=self.mypress)
	self.bind(on_release=self.myrelease)

    def mypress(self, button):
	print "Pressed"

    def myrelease(self, button):
	print "Released"



if __name__ == '__main__':

    from kivy.app import App
    class TestApp(App):

        def build(self):
            self.root = MyButton(text='hello world')
            return self.root

    app = TestApp()
    app.run()

