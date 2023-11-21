from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label



class TimeZoneAlarmApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        layout.background_color = (0.95, 0.95, 0.95, 1)  # Light gray background color

    

        self.label = Label(text="Selected Time: ", color=(0.2, 0.6, 1, 1))  # Blue text color

        self.set_alarm_button = Button(
            text="Set Alarm",
            on_press=self.set_alarm,
            background_color=(0.2, 0.6, 1, 1),  # Blue background color
            color=(1, 1, 1, 1),  # White text color
            size_hint=(1, None),
            height=50,
        )

        
        layout.add_widget(self.label)
        layout.add_widget(self.set_alarm_button)

        return layout

    def on_time_selected(self, instance, value):
        # Handle the selected time and perform time zone conversion if needed
        pass

    def set_alarm(self, instance):
        # Implement the logic to set the alarm based on the selected time and time zone
        pass


if __name__ == '__main__':
    TimeZoneAlarmApp().run()
