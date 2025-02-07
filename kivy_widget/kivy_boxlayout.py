from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class BoxLayoutExample(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=20, spacing=10, **kwargs)

        self.add_widget(Button(text="Tombol 1"))
        self.add_widget(Button(text="Tombol 2"))
        self.add_widget(Button(text="Tombol 3"))

class BoxLayoutApp(App):
    def build(self):
        return BoxLayoutExample()

BoxLayoutApp().run()
