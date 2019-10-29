# Submitter: jaredac1 (Clark, Jared)
# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole


class Pulsator(Black_Hole): 
    counter=30
    def __init__(self,x,y):
        Black_Hole.__init__(self,x,y)
        self.counter=Pulsator.counter
    
    def update(self,model):
        if len(Black_Hole.update(self,model))==0:
            self.counter-=1
            if self.counter==0:
                self.change_dimension(-1, -1)
                self.counter=Pulsator.counter
                w,h=self.get_dimension()
                if w==0:
                    model.remove(self)
        else:
            self.counter=Pulsator.counter
            self.change_dimension(len(Black_Hole.update(self,model)), 
                                  len(Black_Hole.update(self,model)))
            self.eaten=set()
