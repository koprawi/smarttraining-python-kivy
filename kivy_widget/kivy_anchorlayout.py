from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button

class AnchorLayoutExample(AnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(anchor_x="center", anchor_y="bottom", **kwargs)

        self.add_widget(Button(text="Tombol di Bawah"))

class AnchorLayoutApp(App):
    def build(self):
        return AnchorLayoutExample()

AnchorLayoutApp().run()
