import datetime
from kivy.app import App
from kivy.uix.widget import Widget 
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from functools import partial
from kivy.lang import Builder
from kivy.effects.opacityscroll import OpacityScrollEffect
from kivy.properties import ObjectProperty
Window.size = (200,100)
Builder.load_string('''
<TimePicker>
	ScrollView:
		do_scroll_x:False
		do_scroll_y:True
		smooth_scroll_end : 7
		bar_color:[1,1,1,0]
		GridLayout:
			id:vl1
			size_hint_y:None
			rows: 0  #change this to set the number of Ev_rows 
			height: self.minimum_height
			row_default_height: 42
			spacing: 2.5
	Label:
		text:":"
		size_hint_x:0.2
	MyView:
		do_scroll_x:False
		do_scroll_y:True
		smooth_scroll_end : 10
		bar_color:[1,1,1,0]
		GridLayout:
			id:vl2
			size_hint_y:None
			rows: 0  #change this to set the number of Ev_rows 
			height: self.minimum_height
			row_default_height: 42
			spacing: 2.5
	BoxLayout:
		orientation:"vertical"
		pos_hint:{'center_x':.8,'center_y':.5}
		GridLayout:
			id:vl3
			rows:2
	''')
class MyView(ScrollView):
	def __init__(self,**kwargs):
		super(MyView,self).__init__(**kwargs)
class TimePicker(BoxLayout):
	def __init__(self,**kwargs):
		super(TimePicker,self).__init__(**kwargs)
		for i in range(1,13):
			btn = Button(text = str(i),on_press = self.btn_press,background_color = [1,1,1,0])
			self.ids.vl1.rows += 1
			self.ids.vl1.add_widget(btn)
		for i in range(1,61):
			btn = Button(text = str(i),on_press = self.btn_press,background_color = [1,1,1,0])
			self.ids.vl2.rows += 1
			self.ids.vl2.add_widget(btn)
		AM = Button(text = "AM",on_press = self.btn_press,background_color = [1,1,1,0])
		PM = Button(text = "PM",on_press = self.btn_press,background_color = [1,1,1,0])
		self.ids.vl3.add_widget(AM)
		self.ids.vl3.add_widget(PM)

	def btn_press(self,instance):
		print(instance.text)
class MyApp(App):
	def build(self):
		return TimePicker()
if __name__ == "__main__":
	MyApp().run()