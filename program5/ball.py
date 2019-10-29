# Submitter: jaredac1 (Clark, Jared)
# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10).


from prey import Prey


class Ball(Prey): 
    radius=5
    def __init__(self,x,y):
        ball=Prey(x,y,10,10,1,5)
        ball.randomize_angle()
        ang=ball.get_angle()
        Prey.__init__(self,x,y,10,10,ang,5)
    
    def update(self,model):
        self.move()
    
    def display(self,canvas):
        x,y=self.get_location()
        canvas.create_oval(x-Ball.radius, 
                           y-Ball.radius,
                           x+Ball.radius, 
                           y+Ball.radius,
                           fill='blue')
