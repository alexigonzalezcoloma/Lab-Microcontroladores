from __future__ import division
from visual import *




def brazo_part1():
    frameBrazo = frame(pos=(0,0,0))
    rod1 = cylinder(frame=frameBrazo,pos=(0,25,0), axis=(0,5,0), radius=80 ,color=color.yellow, length=50)
    rod2 = cylinder(frame=frameBrazo,pos=(0,2,0), axis=(0,5,0), radius=100 ,color=color.blue, length=20)
    rod3 = cylinder(frame=frameBrazo,pos=(0,70,0), axis=(0,5,0), radius=100 ,color=color.blue, length=20)
    sop1=mybox = box(pos=(40,120,0), length=30, height=100, width=70,color=color.yellow)
    sop2=mybox = box(pos=(-40,120,0), length=30, height=100, width=70,color=color.yellow)
    return frameBrazo 

def brazo_part2():
    frameBrazo2 = frame(pos=(0,250,0))
    brazo=box(frame=frameBrazo2,pos=(0,0,0), length=50, height=300, width=80,color=color.blue)
    rod2 = cylinder(frame=frameBrazo2,pos=(-100,-130,0), axis=(1,0,0), radius=10 ,color=color.blue, length=200)
    return frameBrazo2

def brazo_part3():
    frameBrazo3 = frame(pos=(0,420,0))
    brazo=box(frame=frameBrazo3,pos=(0,0,100),length=50, height=50, width=300,color=color.yellow)
    return frameBrazo3


Panta = display(title='Brazo Robotico',x=50,y=0,width=1900,height=600,center=(0,0,0))
frameBase = frame(pos=(0,0,0))
Base = box(frame=frameBase,size=(2000,6,2000),color=color.white)
brazo_part1()
brazo_part2()
brazo_part3()
