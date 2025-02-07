from kivy.app import App
from kivy.uix.switch import Switch

class SwitchApp(App):
    def build(self):
        return Switch()

SwitchApp().run()
