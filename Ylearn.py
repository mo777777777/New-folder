import kivy
import arabic_reshaper
import sqlite3
import random
import bidi.algorithm
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.app import runTouchApp
from kivy.uix.widget import Widget




l=['blue','yellow','cyan','green','pink','red','gray','orange','gold','purple','coral','lime','olive','teal','bisque','magenta']
color=random.choice(l)
Window.clearcolor=(color)
Window.size=(400,630)





class WindowManager(ScreenManager):
    pass

class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class LoginWindow(Screen):
    pass


class ErrorWindow(Screen):
    pass

class VidowWindow(Screen):
    pass

class PdfWindow(Screen):
    pass

class QuestionWindow(Screen):
    pass

class Comingsoon(Screen):
    pass


kv=Builder.load_file('Ylearn.kv')
class MyMainApp(App):
    def build(self):
        self.title='mohamed'
        self.icon='Y.png'
        return kv 
    
    
    
    
    
if __name__=='__main__':
    MyMainApp().run()