from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class FloatLayoutExample(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(Button(text="Tombol 1", size_hint=(0.3, 0.2), pos_hint={"x": 0.1, "y": 0.7}))
        self.add_widget(Button(text="Tombol 2", size_hint=(0.3, 0.2), pos_hint={"right": 0.9, "top": 0.9}))

class FloatLayoutApp(App):
    def build(self):
        return FloatLayoutExample()


FloatLayoutApp().run()
