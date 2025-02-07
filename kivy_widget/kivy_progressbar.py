from kivy.app import App
from kivy.uix.progressbar import ProgressBar

class ProgressBarApp(App):
    def build(self):
        return ProgressBar(value=50, max=100)

ProgressBarApp().run()
