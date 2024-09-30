from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.properties import Clock
from kivy.properties import StringProperty, BooleanProperty
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.graphics.context_instructions import Color
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
    text_input_str = StringProperty("Boo")
    # slider_value_text = StringProperty("Value")
    
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
    
    # def on_slider_value (self, widget):
    #     print("Slider : " + str(int(widget.value)))
    #     self.slider_value_text = str(int(widget.value))

    def on_text_validate (self, widget):
        self.text_input_str = widget.text



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



class CanvasExample01 (Widget):
    pass


class CanvasExample02 (Widget):
    pass


class CanvasExample03 (Widget):
    pass


class CanvasExample04 (Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(100, 100, 400, 500), width=2)
            Color(0, 1, 0)
            Line(circle=(300, 200, 50), width=2)
            Color(1, .5, 0)
            Line(rectangle=(400, 50, 200, 100), width=3)
            self.rect = Rectangle(pos=(500, 300), size=(100, 150))
    
    def on_button_a_click (self):
        x, y = self.rect.pos
        w, h = self.rect.size
        inc = dp(5)
        gap = self.width - (x+w)
        print("Gap is : " + str(gap) + "Increment is : " + str(inc))
        if gap < inc:
            inc = gap
        x += inc
        self.rect.pos = (x, y)



class CanvasExample05 (Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        with self.canvas:
            self.ball = Ellipse(pos=self.center, size=(self.ball_size, self.ball_size))
        Clock.schedule_interval(self.update, 1/30)

    def on_size (self, *args):
        print("on size : " + str(self.width) + ", " + str(self.height))
        self.ball.pos = (self.center_x-self.ball_size/2, self.center_y-self.ball_size/2)

    def update (self, dt):
        # print("update")
        x, y = self.ball.pos
        self.ball.pos = (x+5,y)

TheLabApp().run()