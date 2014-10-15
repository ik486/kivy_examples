from kivy.uix.button import Button


class MyButton(Button):
    def __init__(self, **kwargs):
        super(MyButton, self).__init__(**kwargs)

    def on_press(self):
	print "Pressed"

    def on_release(self):
	print "Released"



if __name__ == '__main__':

    from kivy.app import App
    class TestApp(App):

        def build(self):
            self.root = MyButton(text='hello world')
            return self.root

    app = TestApp()
    app.run()

