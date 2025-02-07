import re
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class RegistrationForm(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=20, spacing=10, **kwargs)
        
        # Grid Layout untuk Form
        form_layout = GridLayout(cols=2, spacing=10)
        
        # Nama Lengkap
        form_layout.add_widget(Label(text="Nama Lengkap:"))
        self.name_input = TextInput(hint_text="Masukkan nama lengkap", multiline=False)
        form_layout.add_widget(self.name_input)

        # Email
        form_layout.add_widget(Label(text="Email:"))
        self.email_input = TextInput(hint_text="Masukkan email", multiline=False)
        self.email_input.bind(text=self.validate_email)
        form_layout.add_widget(self.email_input)

        # Jenis Kelamin
        form_layout.add_widget(Label(text="Jenis Kelamin:"))
        self.gender_spinner = Spinner(text="Pilih", values=("Laki-laki", "Perempuan", "Lainnya"))
        form_layout.add_widget(self.gender_spinner)

        # Setuju dengan syarat & ketentuan
        form_layout.add_widget(Label(text="Setuju dengan syarat & ketentuan:"))
        self.terms_checkbox = CheckBox()
        form_layout.add_widget(self.terms_checkbox)

        self.add_widget(form_layout)

        # Tombol Submit
        submit_button = Button(text="Submit", size_hint=(1, 0.3))
        submit_button.bind(on_press=self.submit_form)
        self.add_widget(submit_button)

    def validate_email(self, instance, value):
        """
        Fungsi untuk validasi format email.
        Jika email tidak valid, teks berubah warna menjadi merah.
        """
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_regex, value) and value:
            instance.foreground_color = (1, 0, 0, 1)  # Warna merah jika tidak valid
        else:
            instance.foreground_color = (0, 0, 0, 1)  # Warna hitam jika valid

    def submit_form(self, instance):
        """
        Fungsi untuk menangani tombol submit.
        Jika semua input valid, tampilkan hasil input di dalam popup.
        """
        name = self.name_input.text.strip()
        email = self.email_input.text.strip()
        gender = self.gender_spinner.text
        agree = self.terms_checkbox.active

        # Validasi input
        if not name or not email or gender == "Pilih" or not agree:
            self.show_popup("Error", "Harap isi semua bidang dan setujui syarat & ketentuan.")
            return

        # Validasi email
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_regex, email):
            self.show_popup("Error", "Format email tidak valid.")
            return

        # Menampilkan hasil input
        result_text = f"Nama: {name}\nEmail: {email}\nJenis Kelamin: {gender}\nSetuju: {'Ya' if agree else 'Tidak'}"
        self.show_popup("Hasil Form", result_text)

    def show_popup(self, title, message):
        """
        Fungsi untuk menampilkan popup dengan pesan tertentu.
        """
        popup_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        popup_layout.add_widget(Label(text=message))
        close_button = Button(text="Tutup", size_hint=(1, 0.3))
        popup = Popup(title=title, content=popup_layout, size_hint=(0.6, 0.4))
        close_button.bind(on_press=popup.dismiss)
        popup_layout.add_widget(close_button)
        popup.open()

class RegistrationApp(App):
    def build(self):
        return RegistrationForm()

if __name__ == "__main__":
    RegistrationApp().run()
