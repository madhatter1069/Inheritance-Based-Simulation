# Submitter: jaredac1 (Clark, Jared)
#Special eats a single prey then creates ten more prey of float or ball randomly and then dies. The new prey can be a floater or ball.

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from random import randint

class Special(Black_Hole):
    def __init__(self,x,y):
        Black_Hole.__init__(self,x,y)
        
    def update(self,model):
        if len(Black_Hole.update(self,model))!=0:
            for i in range(len(Black_Hole.update(self,model))):
                for a in range(10):
                    choice=randint(1,2)
                    dx=randint(-10,10)
                    dy=randint(-10,10)
                    if choice==1:
                        model.simuls.add(Ball(self._x+dx,self._y+dy))
                    elif choice==2:
                        model.simuls.add(Floater(self._x+dx,self._y+dy))
            self.eaten=set()
            model.remove(self)
        
    def display(self,canvas):
        x,y=self.get_location()
        canvas.create_oval(x-Black_Hole.radius, 
                           y-Black_Hole.radius,
                           x+Black_Hole.radius, 
                           y+Black_Hole.radius,
                           fill='purple')
            
            
            
            
            