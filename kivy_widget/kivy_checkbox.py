from kivy.app import App
from kivy.uix.checkbox import CheckBox

class CheckBoxApp(App):
    def build(self):
        return CheckBox()

CheckBoxApp().run()
