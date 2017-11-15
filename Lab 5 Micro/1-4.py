from __future__ import division
from visual import *
import serial

Panta     = display(title='Brazo Robotico',x=50,y=0,width=640,height=640,center=(0,0,0))
frameBase = frame(pos = (0,0,0))
Base      = box(frame=frameBase,size=(1000,6,1000),color=color.white)


def  MAP(x,vi,vf,vis,vfs):
    return(x-vi)*(vfs-vis)/(vf-vi)+vis

def Base():
    f=frame(pos=(0,0,0))
    f.rod1 = cylinder(frame=f,pos=(0,25,0), axis=(0,5,0), radius=80  ,color=color.yellow, length=50)
    f.rod2 = cylinder(frame=f,pos=(0,2,0 ), axis=(0,5,0), radius=100 ,color=color.blue,   length=20)
    f.rod3 = cylinder(frame=f,pos=(0,70,0), axis=(0,5,0), radius=100 ,color=color.blue,   length=20)

    f.sop1=mybox = box(frame=f, pos=(40,120,0 ), length=30, height=100, width=70,color=color.yellow)
    f.sop2=mybox = box(frame=f, pos=(-40,120,0), length=30, height=100, width=70,color=color.yellow)
    return f

def Brazo1(f):
    f2        = frame(frame=f , pos=(2,300,0))
    f2.brazo1 =   box(frame=f2, pos=(0,0,0), length=50, height=500, width=80,color=color.blue)
    
    return f2

def Brazo2(f):
    f3        = frame(frame = f , pos = (2,90,0))
    f3        = frame(frame = f , pos = (-38,150,110))
    f3.brazo2 =   box(frame = f3, pos = (0,0,0), length=45, height=60, width=300,color = color.yellow)
    return f3

def Brazo3(f):
    f4      =    frame(frame=f , pos=(0,0,110))
    f4.rod3 = cylinder(frame=f4, pos=(0,0,0) , axis=(0,0,5), radius=60, color=color.red, length=50)
    f4.box1 =      box(frame=f4, pos=(0,0,60), length=40, height=40,  width=40,color=color.green)
    f4.line =      box(frame=f4, pos=(0,0,70), length=10, height=100, width=10,color=color.white)
    return f4
puerto=serial.Serial(0,9600)
    
parte1 = Base()
parte2 = Brazo1(parte1)
parte3 = Brazo2(parte2)
parte4 = Brazo3(parte3)
fr     = frame(pos = (0,0,0))
b=0
# part 1  de 0 a 360 part 2 de 0 a45 part3 -90 a 45 part4 de 0 a 360
parte2.rotate(angle = math.radians(45), axis=(1,0,0), origin = (39,118,-25))
parte3.rotate(angle = math.radians(45), axis=(1,0,0), origin = (0 ,140,-10))
parte4.rotate(angle = math.radians(), axis=(0,0,1), origin = parte4.pos )

while True:
    grados_1=int(puerto.readline()[0])
    grados_2=int(puerto.readline()[1])
    grados_3=int(puerto.readline()[2])
    grados_4=int(puerto.readline()[3])
    rate(10);    
    #parte1.rotate(angle = math.radians(2), axis=(0,1,0), origin = parte1.pos)
    parte2.rotate(angle = math.radians(), axis=(1,0,0), origin = (39,118,-25))
    #parte3.rotate(angle = math.radians(), axis=(1,0,0), origin = (0 ,140,-10))
    #parte4.rotate(angle = math.radians(), axis=(0,0,1), origin = parte4.pos  )
