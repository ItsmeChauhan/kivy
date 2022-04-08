import kivy
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.app import App
class himanGrid(GridLayout):
	def __init__(self,**kwargs):
		super(himanGrid,self).__init__()
		self.cols =2
		self.add_widget(Label(text="hello"))
		self.student = TextInput()
		self.add_widget(self.student)
		
		
		
		self.press =Button(text="click me")
		self.add_widget(self.press)
		def click_me(self,instance):
			
		     self.press.bind(on_press=self.click_me)
		     print("hell"+self.click_me.text)
		 








class himanshuApp(App):
	 def build (self):
		 return himanGrid()
		
		
if __name__ =="__main__":
	himanshuApp().run()		