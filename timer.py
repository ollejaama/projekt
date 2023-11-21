import pygame
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.pickers import MDTimePicker
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.clock import Clock
import datetime

Window.size = (350, 600)

KV = '''
ScreenManager:
    MenuScreen:
    AlarmScreen1:
    AlarmScreen2:

<MenuScreen>:
    name: 'menu'
    MDFloatLayout:
        md_bg_color: 1, 1, 1, 1
        MDIconButton:
            icon: "tallink.png"
            icon_size: "70sp"
            pos_hint: {"center_x": .75, "center_y": .5}
            on_release: root.manager.current = 'alarm1'

        MDIconButton:
            icon: "dfds.png"
            icon_size: "80sp"
            pos_hint: {"center_x": .3, "center_y": .5}
            on_release: root.manager.current = 'alarm2'

<AlarmScreen1>:
    name: 'alarm1'
    MDFloatLayout:
        md_bg_color: 1, 1, 1, 1
        MDIconButton:
            icon: "nool.png"
            icon_size: "30sp"
            pos_hint: {"center_x": .13, "center_y": .94}
            md_bg_color: 0, 0, 0, 0
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            on_release: app.switch_screen('menu')
            
        MDLabel:
            text: "Hommikusöök kell 7-9"
            font_size: "15sp"
            pos_hint: {"center_y": .935}
            halign: "center"
            bold: False
        MDIconButton:
            icon: "plus.png"
            icon_size: "40sp"
            pos_hint: {"center_x": .87, "center_y": .94}
            md_bg_color: 0, 0, 0, 0
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            on_release: app.schedule()
        MDLabel:
            id: alarm_time_2
            text: ""
            pos_hint: {"center_y": .5}
            halign: "center"
            font_size: "30sp"
            bold: True
        MDRaisedButton:
            text: "Stop"
            pos_hint: {"center_x": .5, "center_y": .2}
            on_release: app.stop()
<AlarmScreen2>:
    name: 'alarm2'
    MDFloatLayout:
        md_bg_color: 1, 1, 1, 1
        MDIconButton:
            icon: "nool.png"
            icon_size: "30sp"
            pos_hint: {"center_x": .13, "center_y": .94}
            md_bg_color: 0, 0, 0, 0
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            on_release: app.switch_screen('menu')
        MDLabel:
            text: "Hommikusöök kell 7-8"
            font_size: "15sp"
            pos_hint: {"center_y": .935}
            halign: "center"
            bold: False
        MDIconButton:
            icon: "plus.png"
            icon_size: "40sp"
            pos_hint: {"center_x": .87, "center_y": .94}
            md_bg_color: 0, 0, 0, 0
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            on_release: app.schedule()
        MDLabel:
            id: alarm_time_1
            text: ""
            pos_hint: {"center_y": .5}
            halign: "center"
            font_size: "30sp"
            bold: True
        MDRaisedButton:
            text: "Stop"
            pos_hint: {"center_x": .5, "center_y": .24}
            on_release: app.stop()
'''

class MenuScreen(Screen):
    def rickroll(self):
        print("You've been rickrolled!")

class AlarmScreen1(Screen):
    def on_enter(self):
        app = MDApp.get_running_app()
        app.stop()

class AlarmScreen2(Screen):
    def on_enter(self):
        app = MDApp.get_running_app()
        app.stop()

class Alarm(MDApp):
    pygame.init()
    sound = pygame.mixer.Sound("alarm.mp3")
    volume = 0

    def build(self):
        return Builder.load_string(KV)

    def schedule(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.get_time, on_save=self.start_countdown)
        time_dialog.open()

    def start_countdown(self, instance, time):
        current_screen = self.root.current_screen
        if current_screen.name == 'alarm1':
            current_screen.ids.alarm_time_1.text = str(time)
        elif current_screen.name == 'alarm2':
            current_screen.ids.alarm_time_2.text = str(time)

        seconds = (time.hour * 3600) + (time.minute * 60) + time.second
        Clock.schedule_once(self.alarm, seconds)

    def alarm(self, *args):
        print("Alarm!")
        self.start()

    def set_volume(self, *args):
        self.volume += 0.05
        if self.volume < 1.0:
            Clock.schedule_interval(self.set_volume, 10)
            self.sound.set_volume(self.volume)
            print(self.volume)
        else:
            self.sound.set_volume(1)
            print("Jõuidsin max voluumini!")

    def start(self, *args):
        self.sound.play(-1)
        self.set_volume()

    def stop(self):
        self.sound.stop()
        Clock.unschedule(self.set_volume)
        self.volume = 0

    def get_time(self, instance, time):
        pass  # No need to update the time label here

    def switch_screen(self, screen_name):
        self.root.current = screen_name


Alarm().run()