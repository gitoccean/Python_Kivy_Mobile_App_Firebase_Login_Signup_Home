from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyD9N2IBF0NS-9FZMbFIW_ON1Tq94rkXZOY",
    'authDomain': "pythonauthproject-c3fc8.firebaseapp.com",
    'databaseURL': "https://pythonauthproject-c3fc8-default-rtdb.firebaseio.com/",
    'projectId': "pythonauthproject-c3fc8",
    'storageBucket': "pythonauthproject-c3fc8.appspot.com",
    'messagingSenderId': "679814430731",
    'appId': "1:679814430731:web:9790480fa660f4cc41870e"
}

firebase = pyrebase.initialize_app(firebaseConfig)
mAuth = firebase.auth()


class SignupScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


class HomeScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(SignupScreen(name='signup'))
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(HomeScreen(name='home'))


# App Controller
class SignupPage(App):
    def build(self):
        Window.size = (400, 600)
        return Builder.load_file("kvapp.kv")

    # signup function
    def signup(self, em, ps, msg):
        try:
            mAuth.create_user_with_email_and_password(email=em.text, password=ps.text)
            print("User created.")
            msg.text("User created.")
            em.text = ""
            ps.text = ""
        except:
            print("Email already exist.")

    # login function
    def login(self, em, ps, msg):
        try:
            print(em.text)
            print(ps.text)
            mAuth.sign_in_with_email_and_password(email=em.text, password=ps.text)
            print('Login')
            self.root.current = 'home'
        except:
            msg.text = "Invalid Credentials."
            msg.color = 'red'
            print("Invalid Credentials.")


# run
SignupPage().run()
