import os
import sys
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window


class MyBoxLayout(BoxLayout):
	def __init__(self,**kwargs):
		super(MyBoxLayout,self).__init__(**kwargs)
		self.orientation='vertical'
		self.spacing=1
		self.size_hint_y=None
		files=os.listdir('.')		
		self.height=(100*len(files))+len(files)
		buttons=list()
		for a in files:
			buttons.append(Button(text=a,size_hint=(1,None),height=100))
			buttons[-1].bind(on_press=openFile)
			self.add_widget(buttons[-1])
			
		
			


class MyScrollView(ScrollView):
	def __init__(self,**kwargs):
		super(MyScrollView,self).__init__(**kwargs)
		self.do_scroll_x=False
		self.do_scroll_y=True
		self.size_hint=[1,1]
		self.bar_width=20
		self.scroll_type=['bars']
		self.add_widget(MyBoxLayout())







class OdApp(App):
	def build(self):
		return MyScrollView()

def openFile(instance):
	print(os.popen("alacritty --title "+instance.text+ " -e nvim "+instance.text))



if __name__=="__main__":
	OdApp().run()
