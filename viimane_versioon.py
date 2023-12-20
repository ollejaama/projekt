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
    MenuScreen1:
    MenuScreen2:
    AlarmScreen1:
    AlarmScreen2:
    AlarmScreen3:
    AlarmScreen4:
<MenuScreen>:
    name: 'menu'
    MDFloatLayout:
        md_bg_color: 1, 1, 1, 1
        MDIconButton:
            icon: "tallink.png"
            icon_size: "70sp"
            pos_hint: {"center_x": .75, "center_y": .5}
            on_release: root.manager.current = 'menu1'

        MDIconButton:
            icon: "dfds.png"
            icon_size: "80sp"
            pos_hint: {"center_x": .3, "center_y": .5}
            on_release: root.manager.current = 'menu2'
        

<MenuScreen1>:
    name: "menu1"
    MDFloatLayout:
        md_bg_color: 1, 1, 1, 1
        MDFlatButton:
            text: "TALLINN-STOCKHOLM"
            theme_text_color: "Custom"
            text_color: "blue"
            pos_hint: {"center_x": .3, "center_y": .5}
            on_release: root.manager.current = 'alarm1'

        MDFlatButton:
            text: "STOCKHOLM-TALLINN"
            theme_text_color: "Custom"
            text_color: "orange"
            pos_hint: {"center_x": .7, "center_y": .5}
            on_release: root.manager.current = 'alarm3'

        MDIconButton:
            icon: "nool.png"
            icon_size: "30sp"
            pos_hint: {"center_x": .13, "center_y": .937}
            md_bg_color: 0, 0, 0, 0
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            on_release: app.switch_screen('menu')

<MenuScreen2>:
    name: "menu2"
    MDFloatLayout:
        md_bg_color: 1, 1, 1, 1
        MDFlatButton:
            text: "PALDISKI-KAPPELSKÄR"
            theme_text_color: "Custom"
            text_color: "blue"
            pos_hint: {"center_x": .5, "center_y": .8}
            on_release: root.manager.current = 'alarm2'

        MDFlatButton:
            text: "KAPPELSKÄR-PALDISKI"
            theme_text_color: "Custom"
            text_color: "orange"
            pos_hint: {"center_x": .5, "center_y": .2}
            on_release: root.manager.current = 'alarm4'
        
        MDIconButton:
            icon: "nool.png"
            icon_size: "30sp"
            pos_hint: {"center_x": .13, "center_y": .937}
            md_bg_color: 0, 0, 0, 0
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            on_release: app.switch_screen('menu')

<AlarmScreen1>:
    name: "alarm1"    
    MDFloatLayout:
        md_bg_color: 1, 1, 1, 1
        MDLabel:
            text: "TALLINNK(TAL-STCH)"
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
            pos_hint: {"center_x": .13, "center_y": .937}
            md_bg_color: 0, 0, 0, 0
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            on_release: app.switch_screen('menu1')
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
    name: "alarm2"
    MDFloatLayout:
        md_bg_color: 1, 1, 1, 1
        MDLabel:
            text: "DFDS(PAL-KAP)"
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
            pos_hint: {"center_x": .13, "center_y": .937}
            md_bg_color: 0, 0, 0, 0
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            on_release: app.switch_screen('menu2')
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

<AlarmScreen3>:
    name: "alarm3"
    MDFloatLayout:
        md_bg_color: 1, 1, 1, 1
        MDLabel:
            text: "TALLINK(STCH-TAL)"
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
            pos_hint: {"center_x": .13, "center_y": .937}
            md_bg_color: 0, 0, 0, 0
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            on_release: app.switch_screen('menu1')
        MDLabel:
            id: alarm_time3
            text: ""
            pos_hint: {"center_y": .5}
            halign: "center"
            font_size: "30sp"
                
        MDRaisedButton:
            text: "Lõpeta"
            pos_hint: {"center_x": .5, "center_y": .2}
            on_release: app.stop()
<AlarmScreen4>:
    name: "alarm4"
    MDFloatLayout:
        md_bg_color: 1, 1, 1, 1
        MDLabel:
            text: "DFDS(KAP-PAL)"
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
            on_release: app.switch_screen('menu2')
        MDLabel:
            id: alarm_time4
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

class MenuScreen1(Screen):
    def rickroll(self):
        print("You've been rickrolled!")

class MenuScreen2(Screen):
    def rickroll(self):
        print("You've been rickrolled!")
    

class AlarmScreen1(Screen):
    def on_enter(self):
        print("You've been rickrolled!")    
        

class AlarmScreen2(Screen):
    def on_enter(self):
        print("You've been rickrolled!")

class AlarmScreen3(Screen):
    def on_enter(self):
        print("You've been rickrolled!")  

class AlarmScreen4(Screen):
    def on_enter(self):
        print("You've been rickrolled!")
       


class Alarm(MDApp):

    pygame.init()
    sound = pygame.mixer.Sound("alarm.mp3")
    volume = 1
    alarm_scheduled = None  # Planeeritud alarmi sündmuse muutuja
    alarm = None  # Valitud alarmiaja muutuja

    def build(self):
        return Builder.load_string(KV)

    def time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.get_time, on_save=self.schedule)
        time_dialog.open()

    def schedule(self, *args):
        # Katkestab eelnevad pandud alarmid
        if self.alarm_scheduled:
            Clock.unschedule(self.alarm_scheduled)

        # Võtab valitud alarmiaja
        if isinstance(self.alarm, str):
            alarmi_str = self.alarm
            
        
            alarmi_aeg = datetime.datetime.strptime(alarmi_str, "%H:%M:%S")

            # Leiab praeguse aja
            current_time = datetime.datetime.now()

            # Arvutab aja järgmise alarmini
            time_difference = (alarmi_aeg - current_time).total_seconds()

            time_difference = time_difference % (24 * 3600)   # Teeb kindlaks, et aeg oleks 24-h periood
            current_screen = self.root.current_screen
            if current_screen.name == 'alarm1':
                aeg = time_difference + 3600
            elif current_screen.name == 'alarm2':
                aeg = time_difference - 3600
            elif current_screen.name == 'alarm3':
                aeg = time_difference - 3600
            elif current_screen.name == 'alarm4':
                aeg = time_difference - 3600
            print(aeg)
            print(time_difference)
            self.alarm_scheduled = Clock.schedule_once(self.start, aeg)
           
            if current_screen.name == 'alarm1':
                current_screen.ids.alarm_time.text = f"{alarmi_str} rootsi aja järgi"
            elif current_screen.name == 'alarm2':
                current_screen.ids.alarm_time1.text = alarmi_str
            elif current_screen.name == 'alarm3':
                current_screen.ids.alarm_time3.text = alarmi_str
            elif current_screen.name == 'alarm4':
                current_screen.ids.alarm_time4.text = alarmi_str
        else:
            # Kui aega ei ole valitud, siis mine tagasi põhilehele
            current_screen = self.root.current_screen
            if current_screen.name == 'alarm1':
                current_screen.ids.alarm_time.text = "vali aeg, põmmpea"
            elif current_screen.name == 'alarm2':
                current_screen.ids.alarm_time1.text = "vali aeg, põmmpea"
            elif current_screen.name == 'alarm3':
                current_screen.ids.alarm_time3.text = "vali aeg, põmmpea"
            elif current_screen.name == 'alarm4':
                current_screen.ids.alarm_time4.text = "vali aeg, põmmpea"
            
            print("Lol")

    def alarm(self, *args):
        self.start()

    def start(self, *args):
        self.sound.play(-1)

    def stop(self):
        # Katkestab planeeritud alarmid
        if self.alarm_scheduled:
            Clock.unschedule(self.alarm_scheduled)

        self.sound.stop()
        self.volume = 0
        self.alarm = None  # resettib valitud alarmiaja
        
        current_screen = self.root.current_screen
        
        
        if current_screen.name == 'alarm1':
            current_screen.ids.alarm_time.text = "lõpetatud!"
        if current_screen.name == 'alarm2':
            current_screen.ids.alarm_time1.text = "lõpetatud!"
        if current_screen.name == 'alarm3':
            current_screen.ids.alarm_time3.text = "lõpetatud!"
        if current_screen.name == 'alarm4':
            current_screen.ids.alarm_time4.text = "lõpetatud!"

    def get_time(self, instance, time):
        self.alarm = str(time)
        
    def switch_screen(self, screen_name):
        self.root.current = screen_name

Alarm().run()
