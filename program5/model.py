# Submitter: jaredac1 (Clark, Jared)
import controller, sys
import model   # We need a reference to this module to pass it to update methods

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from special   import Special
from cProfile  import run


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
run=False
obj=None
simuls=set()
cycle_count=0

#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global run,cycle_count,simuls,obj
    run=False
    cycle_count=0
    simuls=set()
    obj=None
    


#start running the simulation
def start ():
    global run
    run=True


#stop running the simulation (freezing it)
def stop ():
    global run
    run=False


#step just one update in the simulation
def step ():
    global run 
    if run==True:
        update_all()
        stop()
    else:
        run=True
        step()


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global obj
    obj=kind


#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    global simuls,obj
    try:
        if obj=='Remove':
            for thing in simuls:
                if thing.contains((x,y)):
                    simuls.remove(thing)
        else:
            thing=eval(obj)
            created=thing(x,y)
            simuls.add(created)
            
    except RuntimeError:
        pass
    except TypeError:
        pass
    
#add simulton s to the simulation
def add(s):
    global simuls 
    simuls.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    global simuls 
    simuls.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    want=set()
    global simuls 
    for item in simuls:
        if p(item):
            want.add(item)
    return want


#call update for every simulton in the simulation (pass each model)
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def update_all():
    global cycle_count
    try:
        if run:
            cycle_count+=1
            for item in simuls:
                item.update(model)
    except RuntimeError:
        pass


#delete every simulton being simulated from the canvas; next call display on every
#  simulton being simulated to add it back to the canvas, possibly in a new location, to
#  animate it; also, update the progress label defined in the controller
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for item in simuls:
        item.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(len(simuls))+' balls/'+str(cycle_count)+' cycles')
    

