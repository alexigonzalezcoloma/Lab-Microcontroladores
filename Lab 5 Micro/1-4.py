from __future__ import division
from visual import *

Panta = display(title='Brazo Robotico',x=50,y=0,width=640,height=640,center=(0,0,0))
frameBase = frame(pos=(0,0,0))
Base = box(frame=frameBase,size=(1000,6,1000),color=color.white)


def Base():
    f=frame(pos=(0,0,0))
    f.rod1 = cylinder(frame=f,pos=(0,25,0), axis=(0,5,0), radius=80 ,color=color.yellow, length=50)
    f.rod2 = cylinder(frame=f,pos=(0,2,0), axis=(0,5,0), radius=100 ,color=color.blue, length=20)
    f.rod3 = cylinder(frame=f,pos=(0,70,0), axis=(0,5,0), radius=100 ,color=color.blue, length=20)

    f.sop1=mybox = box(frame=f, pos=(40,120,0), length=30, height=100, width=70,color=color.yellow)
    f.sop2=mybox = box(frame=f, pos=(-40,120,0), length=30, height=100, width=70,color=color.yellow)
    return f

def Brazo1(f):
    f.brazo1 = box(frame=f,pos=(0,240,0), length=50, height=500, width=80,color=color.blue)
    f.brazo2 = box(frame=f,pos=(-40,450,110), length=45, height=60, width=300,color=color.yellow)
    return f

def Brazo2(f):
    #f=frame(pos=(-40,450,230))
    f= frame(pos=(26,472,260))
    f=frame(pos=(0,0,0))
    f.rod3 = cylinder(frame=f,pos=(-40,455,250), axis=(0,0,5), radius=60 ,color=color.red, length=50)
    f.box1 = box(frame=f, pos=(-40,455,310), length=40, height=40, width=40,color=color.green)
    f.line = box(frame=f, pos=(-40,455,320), length=10, height=100, width=10,color=color.white)

    return f

parte1 = Base()
parte2 = Brazo1(parte1)
parte3 = Brazo2(parte2)
while True:
    #get= Panta.mouse.getclick()
    #print get.pos
    rate(10);
    parte1.rotate(angle=math.radians(3), axis=(0,1,0), origin=parte1.pos)
    parte2.brazo2.rotate(angle=math.radians(20), axis=(1,0,0), origin=(51, 450, -2))#parte2.brazo1.pos)

    
