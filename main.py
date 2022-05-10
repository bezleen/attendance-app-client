import re
from telnetlib import STATUS
from urllib import response
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.app import MDApp
from kivymd.uix.list import MDList, IRightBodyTouch, OneLineListItem
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
from kivy.properties import StringProperty
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivy.uix.widget import Widget


Window.size = (360,620)
import os
import execute_api.login as lg
import execute_api.signup as su
import execute_api.user_info as ui
import execute_api.list_class as lc

class Login(Screen):
    def on_leave(self, *args):
        self.clear_widgets()
class Signup(Screen):
    def on_pre_leave(self, *args):
        self.clear_widgets()
class Home(Screen):
    def on_pre_leave(self, *args):
        self.clear_widgets()
class Main(Screen):
    def on_pre_leave(self, *args):
        self.clear_widgets()

class MainApp(MDApp):
    at = ''
    rt = ''
    # def clear_screen(self):
    #     self.clear_widgets()
    def login(self):
        email = self.root.get_screen('login').ids.email.text
        pw = self.root.get_screen('login').ids.pw.text
        response = lg.exec_login('123@gmail.com','123456')
        if response['status'] == 200:
            self.at = response['data']['access_token']
            self.rt = response['data']['refresh_token']
       # elif response['status'] == 401
            
    def signup(self):
        email = self.root.get_screen('signup').ids.email.text
        phone = self.root.get_screen('signup').ids.phone.text
        name = self.root.get_screen('signup').ids.name.text
        pw1 = self.root.get_screen('signup').ids.pw1.text
        pw2 = self.root.get_screen('signup').ids.pw2.text
        if pw1 == pw2:
            response = su.exec_signup(email,pw1,name,phone)
            
            print(response)

    def logout(self):
        self.at = ''
        self.rt = ''
        self.root.get_screen('home').ids.email.text = ''
        self.root.get_screen('home').ids.name.text = ''
        self.root.get_screen('home').ids.phone.text = ''
    #Screen 2
    # def createstudent(self):
        

    #Screen 4    
    def user_info(self):
        response= ui.exec_user_info(self.at)
        if response['status'] == 200:
            avatar = response['data']['avatar']
            email = response['data']['email']
            name = response['data']['name']
            id = response['data']['id']
            phone = response['data']['phone']
            self.root.get_screen('home').ids.email.text = email
            self.root.get_screen('home').ids.name.text = name
            self.root.get_screen('home').ids.phone.text = phone   
        else:
            pass
        # print(self.at)  
        # print(response)
        # print(r)
               
    def list_class_1(self):
        print("1")
        response=lc.exec_list_class(self.at)
        print(response)
        if response['status'] == 200: 
            for i in response['data']:
                name = i['name']
                id = i['id']
                print(name)
                self.root.get_screen('home').ids.container.add_widget(
                    OneLineListItem(text=f"Class {name}"))

                
    def build(self):
        Builder.load_file("main.kv")
        Builder.load_file("login.kv")
        Builder.load_file("signup.kv")
        Builder.load_file("home.kv")
        sm = ScreenManager()
        sm.add_widget(Main(name = 'main'))
        sm.add_widget(Login(name = 'login'))
        sm.add_widget(Signup(name = 'signup'))
        sm.add_widget(Home(name = 'home'))
        return sm
       
if __name__ == "__main__":
    LabelBase.register(name='MPoppins', fn_regular=os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'fonts/Poppins-Medium.ttf'))
    LabelBase.register(name='BPoppins', fn_regular=os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'fonts/Poppins-SemiBold.ttf'))
    # LabelBase.register(name='BPoppins', fn_regular="fontsPoppins-SemiBold.ttf")
    MainApp().run()