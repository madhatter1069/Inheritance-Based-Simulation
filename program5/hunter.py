# Submitter: jaredac1 (Clark, Jared)
# Hunter is derived from the Mobile_Simulton/Pulsator classes: i.e., it updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2



class Hunter(Pulsator,Mobile_Simulton):
    dist=200
    def __init__(self,x,y):
        ball=Mobile_Simulton(x,y,20,20,1,5)
        ball.randomize_angle()
        ang=ball.get_angle()
        Mobile_Simulton.__init__(self,x,y,10,10,ang,5)
        Pulsator.__init__(self, x, y)
    
    def update(self,model):
        chase=set(a for a in model.simuls if isinstance(a,Prey))
        want=set()
        try:
            for item in chase:
                if self.distance(item.get_location())<=Hunter.dist:
                    want.add(item)
            if len(want)==0:
                self.move()
            else:
                fez=min(want,key=lambda prey_on: self.distance(prey_on.get_location()))
                dif_y=fez.get_location()[1]-self.get_location()[1]
                dif_x=fez.get_location()[0]-self.get_location()[0]
                self.set_angle(atan2(dif_y,dif_x))
            Pulsator.update(self,model)
            self.move()
            
        except RuntimeError:
            pass
        
