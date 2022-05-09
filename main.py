import re
from telnetlib import STATUS
from urllib import response
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.app import MDApp
from kivymd.uix.list import OneLineAvatarIconListItem
from kivy.lang import Builder
from kivy.core.window import Window
Window.size = (360,620)

import execute_api.login as lg
import execute_api.signup as su
import execute_api.user_info as ui


class MainApp(MDApp):
    at = ''
    rt = ''
        
        
    def Tabs(MDFloatLayout, MDTabsBase):
        pass  
    def login(self):
        email = self.root.get_screen('login').ids.email.text
        pw = self.root.get_screen('login').ids.pw.text
        response = lg.exec_login(email,pw)
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
        
    def user_info(self):
        response= ui.exec_user_info(self.at)
        print(self.at)  
        print(response)
        
    def button_push(self):
        for i in range (20):
            self.ids.list_one.add_widget(OneLineAvatarIconListItem(text=f'List Item {i}'))
        
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("main.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        screen_manager.add_widget(Builder.load_file("signup.kv"))
        screen_manager.add_widget(Builder.load_file("home.kv"))
        return screen_manager
    
    
if __name__ == "__main__":
    LabelBase.register(name='MPoppins', fn_regular="/home/nhandng/ml_projects/Poppins/Poppins-Medium.ttf")
    LabelBase.register(name='BPoppins', fn_regular="/home/nhandng/ml_projects/Poppins/Poppins-SemiBold.ttf")
    MainApp().run()