from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.spinner import Spinner

class SpinnerApp(App):
    def build(self):
        layout = FloatLayout()  # Menggunakan FloatLayout untuk posisi lebih fleksibel
        
        spinner = Spinner(
            text="Select One",
            values=("Option 1", "Option 2", "Option 3"),
            size_hint=(None, None),  # Menentukan ukuran agar tidak menghilang
            size=(200, 50),  # Ukuran eksplisit untuk tampilan lebih jelas
            pos_hint={"center_x": 0.5, "center_y": 0.5}  # Menempatkan di tengah layar
        )
        
        layout.add_widget(spinner)
        return layout

SpinnerApp().run()
