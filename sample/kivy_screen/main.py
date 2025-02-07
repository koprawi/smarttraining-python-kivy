from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton

KV = """
ScreenManager:
    LoginScreen:
    DashboardScreen:

<LoginScreen>:
    name: "login"
    
    MDBoxLayout:
        orientation: "vertical"
        spacing: dp(20)
        padding: dp(20)
        pos_hint: {"center_y": 0.5}

        MDLabel:
            text: "Login"
            font_style: "H5"
            halign: "center"

        MDTextField:
            id: username
            hint_text: "Username"
            icon_right: "account"
            size_hint_x: None
            width: 300
            pos_hint: {"center_x": 0.5}

        MDTextField:
            id: password
            hint_text: "Password"
            password: True
            icon_right: "eye-off"
            size_hint_x: None
            width: 300
            pos_hint: {"center_x": 0.5}

        MDRaisedButton:
            text: "Login"
            pos_hint: {"center_x": 0.5}
            on_release: app.check_login()

<DashboardScreen>:
    name: "dashboard"

    MDBoxLayout:
        orientation: "vertical"
        spacing: dp(20)
        padding: dp(20)
        pos_hint: {"center_y": 0.5}

        MDLabel:
            text: "Dashboard"
            font_style: "H4"
            halign: "center"

        MDRaisedButton:
            text: "Logout"
            pos_hint: {"center_x": 0.5}
            on_release: app.logout()
"""

class LoginScreen(Screen):
    pass

class DashboardScreen(Screen):
    pass

class LoginApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def check_login(self):
        username = self.root.get_screen("login").ids.username.text
        password = self.root.get_screen("login").ids.password.text

        if username == "admin" and password == "admin":
            self.root.current = "dashboard"  # Pindah ke Dashboard
        else:
            self.show_dialog("Error", "Username atau Password salah!")

    def logout(self):
        self.root.current = "login"  # Kembali ke halaman login

    def show_dialog(self, title, message):
        dialog = MDDialog(
            title=title,
            text=message,
            buttons=[
                MDRaisedButton(text="OK", on_release=lambda x: dialog.dismiss())
            ]
        )
        dialog.open()

if __name__ == "__main__":
    LoginApp().run()
