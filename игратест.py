from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import random
from random import randint
from kivy.clock import mainthread
import time
from kivy.uix.gridlayout import GridLayout
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
f = str(0)
l = str(0)
zaebalo = int(0)
tv1 = 'Чем хотите сыграть?'
def set_data_label(self, tv1):
                self.data_label = str(tv1) + "\n"
def set_data_label2(self, tv2):
         self.data_label2 = str(tv2) + '\n'
def set_data_label3(self, tv3):
         self.data_label3 = str(tv3) + '\n'
def end():
        time.sleep(3)
        MyApp().stop()
KV = """
MyBL: 
        orientation: 'vertical'
        size_hint: (0.95, 0.95)
        pos_hint: {'center_x': 0.5, 'center_y':0.6}
        Label: 
                font_size: "40sp"
                multiline: True
                text_size: self.width*0.98, None
                size_hint_x: 1.0
                size_hint_y: 3
                height: self.texture_size[1] + 15
                text: root.data_label
        Label: 
                font_size: "25sp"
                multiline: True
                text_size: self.width*0.98, None
                size_hint_x: 1.0
                size_hint_y: 1.0
                height: self.texture_size[1] + 15
                text: root.data_label2
        Label: 
                font_size: "30sp"
                multiline: True
                text_size: self.width*0.98, None
                size_hint_x: 1.0
                size_hint_y: 2
                height: self.texture_size[1] + 15
                text: root.data_label3
        Button:
                text: 'Камень!'
                bold: True
                background_color: '#ada587'
                size_hint: (1, 0.5)
                on_press: root.callback1()
                on_release: root.huy()
        Button:
                text: 'Ножницы!'
                bold: True
                background_color: '#cccccc'
                size_hint: (1, 0.5)
                on_press: root.callback2()
                on_release: root.huy()
        Button:
                text: 'Бумага!'
                bold: True
                background_color: '#f2eecb'
                size_hint: (1, 0.5)
                on_press: root.callback()
                on_release: root.huy()
"""
class MyBL(BoxLayout):
        tv1 = 'Чем хотите сыграть?'
        tv2 = 'Счет'
        tv3 = str('0   0')
        data_label = StringProperty(str(tv1))
        data_label2 = StringProperty(str(tv2))
        data_label3 = StringProperty(str(tv3))
        def callback(self): #бумага
                        global f
                        global l
                        global tv1
                        global tv2
                        global tv3
                        d = 3
                        a = randint(1, 3)
                        if a == 1: 
                                tv1 = str('Бот показал камень. \nВы выйграли!')
                                tv2 = 'Счет: '
                                l = int(l) + 1
                                l = str(l)
                                tv3 = l + ' : ' + f
                                set_data_label(self, tv1)
                                set_data_label2(self, tv2)
                                set_data_label3(self, tv3)
                        elif a == 2:
                                tv1 = str('Бот показал ножницы. \nВы проиграли!')
                                tv2 = 'Счет: '
                                f = int(f) + 1
                                f = str(f)
                                tv3 = l + ' : ' + f
                                set_data_label(self, tv1)
                                set_data_label2(self, tv2)
                                set_data_label3(self, tv3)
                        elif a == 3:
                                tv1 = str('Бот показал бумагу. \nНичья!')
                                tv2 = 'Счет: '
                                tv3 = l + ' : ' + f
                                set_data_label(self, tv1)
                                set_data_label2(self, tv2)
                                set_data_label3(self, tv3)
                        if f == 3 or f == '3':
                                tv1 = 'Вы проиграли! \nВ следующий раз повезет больше!'
                                set_data_label(self, tv1)
                                set_data_label2(self, tv2)
                                set_data_label3(self, tv3)
                        if l == 3 or l == '3':
                                tv1 = 'Поздравляем! \nВы победили!'
                                set_data_label(self, tv1)
                                set_data_label2(self, tv2)
                                set_data_label3(self, tv3)
        def callback1(self): #камень 
                        global f
                        global l
                        global tv1
                        global tv2
                        global tv3
                        d = 2
                        a = randint(1, 3)
                        if a == 1: 
                                tv1 = str('Бот показал камень. \nНичья!')
                                tv2 = 'Счет: '
                                tv3 = l + ' : ' + f
                                set_data_label(self, tv1)
                                set_data_label2(self, tv2)
                                set_data_label3(self, tv3)
                        elif a == 2:
                                tv1 = str('Бот показал ножницы. \nВы выйграли!')
                                tv2 = 'Счет: '
                                l = int(l) + 1
                                l = str(l)
                                tv3 = l + ' : ' + f
                                set_data_label(self, tv1)
                                set_data_label2(self, tv2)
                                set_data_label3(self, tv3)
                        elif a == 3:
                                tv1 = str('Бот показал бумагу. \nВы проиграли!')
                                tv2 = 'Счет: '
                                f = int(f) + 1
                                f = str(f)
                                tv3 = l + ' : ' + f
                                set_data_label(self, tv1)
                                set_data_label2(self, tv2)
                                set_data_label3(self, tv3)
        def callback2(self): #ножницы
                        global f
                        global l
                        global tv1
                        global tv2
                        global tv3               
                        d = 1
                        a = randint(1, 3)
                        if a == 1:
                                tv1 = str('Бот показал камень. \nВы проиграли!')
                                tv2 = 'Счет: '
                                f = int(f) + 1
                                f = str(f)
                                tv3 = l + ' : ' + f
                                set_data_label(self, tv1)
                                set_data_label2(self, tv2)
                                set_data_label3(self, tv3)  
                        elif a == 2:
                                tv1 = str('Бот показал ножницы. \nНичья!')
                                tv2 = 'Счет: '
                                tv3 = l + ' : ' + f
                                set_data_label(self, tv1)
                                set_data_label2(self, tv2)
                                set_data_label3(self, tv3)
                        elif a == 3:
                                tv1 = str('Бот показал бумагу. \nВы выйграли!')
                                tv2 = 'Счет: '
                                l = int(l) + 1
                                l = str(l)
                                tv3 = l + ' : ' + f
                                set_data_label(self, tv1)
                                set_data_label2(self, tv2)
                                set_data_label3(self, tv3)  
        def huy(self):
                        if f == 3 or f == '3':
                                end()
                        elif l == 3 or l =='3':
                                end()                       
class MyApp(App): 
        runnung = True
        def build(self):
           return Builder.load_string(KV)
        def on_stop(self): 
                self.running = False
MyApp().run()