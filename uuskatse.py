import pygame
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.pickers import MDTimePicker
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.clock import Clock
import datetime

Window.size = (387, 688)

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
        MDLabel:
            text: "TALLINK"
            font_size: "23sp"
            pos_hint: {"center_y": .935}
            halign: "center"
            bold: False
        MDLabel:
            id: lol
            text: ""
            font_size: "30sp"
            pos_hint: {"center_y": .6}
            halign: "center"
            bold: True
        MDIconButton:
            icon: "kell.png"
            icon_size: "30sp"
            pos_hint: {"center_x": .87, "center_y": .935}
            md_bg_color: 0, 0, 0, 0
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            on_release: app.time_picker()
        MDIconButton:
            icon: "nool.png"
            icon_size: "30sp"
            pos_hint: {"center_x": .13, "center_y": .939}
            md_bg_color: 0, 0, 0, 0
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            on_release: app.switch_screen('menu')
        MDLabel:
            id: alarm_time
            text: ""
            pos_hint: {"center_y": .5}
            halign: "center"
            font_size: "30sp"
                
        MDRaisedButton:
            text: "Lõpeta"
            pos_hint: {"center_x": .5, "center_y": .2}
            on_release: app.stop()
        
<AlarmScreen2>:
    name: 'alarm2'
    MDFloatLayout:
        md_bg_color: 1, 1, 1, 1
        MDLabel:
            text: "DFDS"
            font_size: "23sp"
            pos_hint: {"center_y": .935}
            halign: "center"
            bold: False
        MDLabel:
            id: lol1
            text: ""
            font_size: "30sp"
            pos_hint: {"center_y": .6}
            halign: "center"
            bold: True
        MDIconButton:
            icon: "kell.png"
            icon_size: "30sp"
            pos_hint: {"center_x": .87, "center_y": .935}
            md_bg_color: 0, 0, 0, 0
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            on_release: app.time_picker()
        MDIconButton:
            icon: "nool.png"
            icon_size: "30sp"
            pos_hint: {"center_x": .13, "center_y": .939}
            md_bg_color: 0, 0, 0, 0
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            on_release: app.switch_screen('menu')
        MDLabel:
            id: alarm_time1
            text: ""
            pos_hint: {"center_y": .5}
            halign: "center"
            font_size: "30sp"
                
        MDRaisedButton:
            text: "Lõpeta"
            pos_hint: {"center_x": .5, "center_y": .2}
            on_release: app.stop()
            
        
'''
class MenuScreen(Screen):
    def rickroll(self):
        print("You've been rickrolled!")
    

class AlarmScreen1(Screen):
    def on_enter(self):
        print("You've been rickrolled!")    
        

class AlarmScreen2(Screen):
    def on_enter(self):
        print("You've been rickrolled!")  
       


class Alarm(MDApp):

    pygame.init()
    sound = pygame.mixer.Sound("alarm.mp3")
    volume = 1
    alarm_scheduled = None  # Variable to store scheduled alarm event
    alarm = None  # Variable to store the selected alarm time

    def build(self):
        return Builder.load_string(KV)

    def time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.get_time, on_save=self.schedule)
        time_dialog.open()

    def schedule(self, *args):
        # Cancel any previous scheduled alarm event
        if self.alarm_scheduled:
            Clock.unschedule(self.alarm_scheduled)

        # Get the selected alarm time
        if isinstance(self.alarm, str):
            alarmi_str = self.alarm
            
        
            alarmi_aeg = datetime.datetime.strptime(alarmi_str, "%H:%M:%S")

            # Get the current time
            current_time = datetime.datetime.now()

            # Calculate the time until the next alarm using modular arithmetic
            time_difference = (alarmi_aeg - current_time).total_seconds()

            time_difference = time_difference % (24 * 3600)   # Ensure the time difference is within a 24-hour period
            current_screen = self.root.current_screen
            if current_screen.name == 'alarm1':
                aeg = time_difference + 10
            elif current_screen.name == 'alarm2':
                aeg = time_difference - 3600
            print(aeg)
            print(time_difference)
            self.alarm_scheduled = Clock.schedule_once(self.start, aeg)
           
            if current_screen.name == 'alarm1':
                current_screen.ids.alarm_time.text = f"{alarmi_str} rootsi aja järgi"
            elif current_screen.name == 'alarm2':
                current_screen.ids.alarm_time1.text = alarmi_str
        else:
            # If no time is selected, return to the main page
            current_screen = self.root.current_screen
            if current_screen.name == 'alarm1':
                current_screen.ids.alarm_time.text = "vali aeg, põmmpea"
            elif current_screen.name == 'alarm2':
                current_screen.ids.alarm_time1.text = "vali aeg, põmmpea"
            
            print("Lol")

    def alarm(self, *args):
        self.start()

    def start(self, *args):
        self.sound.play(-1)

    def stop(self):
        # Cancel any scheduled alarm event
        if self.alarm_scheduled:
            Clock.unschedule(self.alarm_scheduled)

        self.sound.stop()
        self.volume = 0
        self.alarm = None  # Reset selected alarm time
        
        current_screen = self.root.current_screen
        
        
        if current_screen.name == 'alarm1':
            current_screen.ids.alarm_time.text = "taun oled"
        if current_screen.name == 'alarm2':
            current_screen.ids.alarm_time1.text = "taun oled"

    def get_time(self, instance, time):
        self.alarm = str(time)
        
    def switch_screen(self, screen_name):
        self.root.current = screen_name

Alarm().run()
