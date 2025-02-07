from kivy.app import App
from kivy.uix.textinput import TextInput

class TextInputApp(App):
    def build(self):
        return TextInput(hint_text="Enter text here")

TextInputApp().run()
