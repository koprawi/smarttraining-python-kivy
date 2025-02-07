from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.image import AsyncImage

class ImageApp(App):
    def build(self):
        img = AsyncImage(source='https://iob.edu.tl/assets/img/logos.png') #untuk gambar online
        #img = Image(source="logo.png") #untuk gambar offline
        return img

ImageApp().run()
