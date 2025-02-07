from kivy.app import App
from kivy.uix.button import Button

class ButtonApp(App):
    def build(self):
        return Button(text="Click Me", font_size=30)

ButtonApp().run()
