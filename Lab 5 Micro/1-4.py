from __future__ import division
from visual import *
import serial

Panta     = display(title='Brazo Robotico',x=50,y=0,width=640,height=640,center=(0,0,0))
frameBase = frame(pos = (0,0,0))
Base      = box(frame=frameBase,size=(1000,6,1000),color=color.white)

#0,360 a 0,45
def map(x,vi,vf,vis,vfs):
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

g1=0
g2=0
g3=0
g4=0

grados=[]
while True:
    parte2.rotate(angle = math.radians(int(0)), axis=(1,0,0), origin = (39,118,-25))
    grados_1=puerto.readline()[:-1]
    grados=grados_1.split(',')
    grados[3].replace('/r','')

    grados_b1=int(grados[0])
    grados_b2=map(int(grados[1]),0,360,0,45)
    grados_b3=map(int(grados[2]),0,360,-90,45)
    grados_b4=int(grados[3])
    
    rate(4);
    if(g1!=grados_b1):
        parte1.rotate(angle = math.radians(grados_b1), axis=(0,1,0), origin = parte1.pos)
    if(g2!=grados_b2):
        parte2.rotate(angle = math.radians(grados_b2), axis=(1,0,0), origin = (39,118,-25))
    if(g3!=grados_b3):
        parte3.rotate(angle = math.radians(grados_b3), axis=(1,0,0), origin = (0 ,140,-10))
    if(g4!=grados_b4):
        parte4.rotate(angle = math.radians(grados_b4), axis=(0,0,1), origin = parte4.pos  )

    g1=grados_b1
    g2=grados_b2
    g3=grados_b3
    g4=grados_b4



     
