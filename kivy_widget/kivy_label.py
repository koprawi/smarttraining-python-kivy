from kivy.app import App
from kivy.uix.label import Label

class LabelApp(App):
    def build(self):
        return Label(text="Hello, Kivy!", font_size=50)

LabelApp().run()
