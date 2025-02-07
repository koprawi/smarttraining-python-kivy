from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivy.uix.image import AsyncImage
from kivy.lang import Builder
import requests

KV = '''
MDScreen:
    md_bg_color: 0.1, 0.1, 0.1, 1  # Tema Gelap

    MDBoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(10)

        MDLabel:
            text: "Weather App"
            font_style: "H5"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1

        MDTextField:
            id: city_input
            hint_text: "Enter City Name"
            mode: "rectangle"
            size_hint_x: 0.9
            pos_hint: {"center_x": 0.5}
            icon_right: "city"

        MDRaisedButton:
            text: "Get Weather"
            size_hint_x: 0.6
            pos_hint: {"center_x": 0.5}
            md_bg_color: 0.2, 0.6, 1, 1
            on_release: app.get_weather()

        MDCard:
            id: weather_card
            size_hint: None, None
            size: dp(320), dp(200)
            pos_hint: {"center_x": 0.5}
            elevation: 10
            padding: dp(15)
            radius: [20]
            opacity: 0  # Awal tidak terlihat

            MDBoxLayout:
                orientation: "vertical"
                spacing: dp(10)
                pos_hint: {"center_x": 0.5}

                AsyncImage:
                    id: weather_icon
                    source: ""
                    size_hint: None, None
                    size: dp(100), dp(100)
                    pos_hint: {"center_x": 0.5}

                MDLabel:
                    id: weather_text
                    text: "Weather information will appear here"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    font_style: "H6"
'''

class WeatherApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"  # Tema Gelap
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)

    def get_weather(self):
        city = self.root.ids.city_input.text.strip()
        if not city:
            self.show_dialog("Error", "Please enter a city name!")
            return

        api_key = "ac7bd4cf6acc84ee58d8d85036a1e878"  # Ganti dengan API Key OpenWeatherMap
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
        try:
            response = requests.get(url)
            data = response.json()

            if data["cod"] == 200:
                weather_desc = data["weather"][0]["description"].capitalize()
                temp = data["main"]["temp"]
                icon_code = data["weather"][0]["icon"]
                icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"

                self.root.ids.weather_text.text = f"{weather_desc}\n{temp}°C"
                self.root.ids.weather_icon.source = icon_url

                # Tampilkan Card dengan Animasi
                self.root.ids.weather_card.opacity = 1

            else:
                self.show_dialog("City Not Found", "Please check the city name and try again.")

        except Exception as e:
            self.show_dialog("Error", str(e))

    def show_dialog(self, title, message):
        dialog = MDDialog(title=title, text=message, size_hint=(0.8, 0.4))
        dialog.open()

if __name__ == '__main__':
    WeatherApp().run()
