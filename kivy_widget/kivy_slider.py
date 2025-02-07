from kivy.app import App
from kivy.uix.slider import Slider

class SliderApp(App):
    def build(self):
        return Slider(min=0, max=100, value=50)

SliderApp().run()
