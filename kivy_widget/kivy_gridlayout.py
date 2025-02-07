from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class GridLayoutExample(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(cols=2, padding=20, spacing=10, **kwargs)

        self.add_widget(Button(text="Tombol 1"))
        self.add_widget(Button(text="Tombol 2"))
        self.add_widget(Button(text="Tombol 3"))
        self.add_widget(Button(text="Tombol 4"))
        self.add_widget(Button(text="Tombol 5"))
        self.add_widget(Button(text="Tombol 6"))

class GridLayoutApp(App):
    def build(self):
        return GridLayoutExample()

GridLayoutApp().run()
