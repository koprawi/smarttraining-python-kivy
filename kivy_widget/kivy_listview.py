from kivy.app import App
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.label import Label

class MyRecycleView(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.viewclass = "Label"  # Setiap item dalam daftar akan menggunakan Label

        self.data = [{"text": f"Item {i}"} for i in range(1, 21)]  # 20 item contoh

        self.layout = RecycleBoxLayout(
            default_size=(None, 40),  # Ukuran item default
            default_size_hint=(1, None),
            size_hint_y=None,
            orientation="vertical"
        )
        self.layout.bind(minimum_height=self.layout.setter("height"))  # Supaya bisa scroll
        self.add_widget(self.layout)

class ListViewApp(App):
    def build(self):
        return MyRecycleView()

if __name__ == "__main__":
    ListViewApp().run()
