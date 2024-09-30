from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.app import App 

class WidgetExample (GridLayout):
    count = 1
    count_enabled = BooleanProperty(False) 
    my_text = StringProperty("1") 
    def on_button_click (self):
        print("Button Cliked")
        if self.count_enabled:
            self.my_text = str(self.count)
            self.count += 1
    def on_toggle_button_state (self, widget):
        print("Toggle State : " + widget.state)
        if widget.state == "normal":
            widget.text = "OFF"
            self.count_enabled = False
        else:
            widget.text = "ON"
            self.count_enabled = True
    def on_switch_active (self, widget):
        print("Switch : " + str(widget.active))

class StackLayoutExample (StackLayout): 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.orientation = "rl-bt"
        for i in range(0, 100):
            size = dp(100)
            b = Button(text=str(i+1), size_hint=(None, None), size=(size, size))
            self.add_widget(b)

# class GridLayoutExample (GridLayout): 
#     pass

class AchorLayoutExample (AnchorLayout): 
    pass

class BoxLayoutExample (BoxLayout):
    pass
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)

    #     b1 = Button(text = "A")
    #     b2 = Button(text = "B")
    #     b3 = Button(text = "C")

    #     self.orientation = 'vertical'
        
    #     self.add_widget(b1)
    #     self.add_widget(b2)
    #     self.add_widget(b3)

class MainWidget (Widget):
    pass

class TheLabApp (App):
    pass

TheLabApp().run()