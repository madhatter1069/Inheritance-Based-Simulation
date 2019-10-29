# Submitter: jaredac1 (Clark, Jared)
# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


from PIL.ImageTk import PhotoImage
from prey import Prey
import random


class Floater(Prey): 
    radius=5
    def __init__(self,x,y):
        self._image=PhotoImage(file='ufo.gif')
        ball=Prey(x,y,10,10,1,5)
        ball.randomize_angle()
        ang=ball.get_angle()
        Prey.__init__(self,x,y,10,10,ang,5)
    
    def update(self,model):
        change_val=random.randint(1,10)
        if change_val>=8:
            self.set_angle(self.get_angle()+random.uniform(-.5,.5))
            current_speed=self.get_speed()
            if current_speed-.5>=3 and current_speed+.5<=7:
                self.set_speed(current_speed+random.uniform(-.5,.5))
        self.move()
    
#     def display(self,canvas):
#         x,y=self.get_location()
#         canvas.create_oval(x-Floater.radius, 
#                            y-Floater.radius,
#                            x+Floater.radius, 
#                            y+Floater.radius,
#                            fill='red')
        
    def display(self,the_canvas):
        the_canvas.create_image(*self.get_location(),image=self._image)
        
        