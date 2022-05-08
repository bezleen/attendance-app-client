from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
Window.size = (360,620)


class Tabs(MDFloatLayout, MDTabsBase):
    pass

class MainApp(MDApp):   
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