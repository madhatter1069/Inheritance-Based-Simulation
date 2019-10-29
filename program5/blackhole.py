# Submitter: jaredac1 (Clark, Jared)
# Black_Hole is derived from Simulton: i.e., it updates by finding and removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):
    radius=10
    def __init__(self,x,y):
        self.eaten=set()
        Simulton.__init__(self,x,y,20,20)
    
    def update(self,model):
        try:
            for item in model.simuls:
                if isinstance(item,Prey):
                    if self.contains(item.get_location()):
                        self.eaten.add(item)
                        model.remove(item)
        except RuntimeError:
            pass
        return self.eaten
          
    def display(self,canvas):
        x,y=self.get_location()
        w,h=self.get_dimension()
        canvas.create_oval(x-w/2, 
                           y-h/2,
                           x+w/2, 
                           y+h/2,
                           fill='black')
    def contains(self,xy):
        return self.distance(xy)<=self.get_dimension()[0]/2
    
    
    
    
    
    
