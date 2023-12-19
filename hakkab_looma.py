import pygame
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.pickers import MDTimePicker
from kivy.clock import Clock
import datetime

Window.size = (750, 600)

KV = '''
MDFloatLayout:
    md_bg_color: 1, 1, 1, 1
    MDLabel:
        text: "ALARM"
        font_size: "30sp"
        pos_hint: {"center_y": .935}
        halign: "center"
        bold: True
    MDLabel:
        id: lol
        text: ""
        font_size: "30sp"
        pos_hint: {"center_y": .6}
        halign: "center"
        bold: True
    MDIconButton:
        icon: "plus"
        pos_hint: {"center_x": .87, "center_y": .94}
        md_bg_color: 0, 0, 0, 1
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        on_release: app.time_picker()
    MDIconButton:
        icon: "nool.png"
        icon_size: "30sp"
        pos_hint: {"center_x": .13, "center_y": .94}
        md_bg_color: 0, 0, 0, 0
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
    MDLabel:
        id: alarm_time
        text: ""
        pos_hint: {"center_y": .5}
        halign: "center"
        font_size: "30sp"
            
    MDRaisedButton:
        text: "Lõpeta"
        pos_hint: {"center_x": .5, "center_y": .4}
        on_release: app.stop()
    
'''

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

            self.alarm_scheduled = Clock.schedule_once(self.start, time_difference)
            self.root.ids.alarm_time.text = alarmi_str
        else:
            # If no time is selected, return to the main page
            self.root.ids.alarm_time.text = "vali aeg, põmmpea"
            print("l")

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
        self.root.ids.alarm_time.text = "taun oled"
        

    def get_time(self, instance, time):
        self.alarm = str(time)
        

Alarm().run()
