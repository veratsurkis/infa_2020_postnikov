import turtle as tr
import numpy as np

tr.shape("turtle")
def circle(x,y,r):
    tr.penup()
    tr.goto(x+r,y)
    tr.pendown()
    for i in range(361):
        tr.goto(x+r*np.cos(i*np.pi/180),y+r*np.sin(i*np.pi/180))

def arc(x,y,r,angle_1,angle_2):
    tr.penup()
    tr.goto(x+r*np.cos(angle_1*np.pi/180),y+r*np.sin(angle_1*np.pi/180))
    tr.pendown()
    for i in range(angle_1,angle_2+1,1):
        tr.goto(x+r*np.cos(i*np.pi/180),y+r*np.sin(i*np.pi/180))
tr.begin_fill()
tr.color('black')
circle(0,0,100)
tr.color('yellow')
tr.end_fill()
for k in range(-1,3,2):
	tr.begin_fill()
	tr.color('black')
	circle(40*k,30,20)
	tr.color('blue')
	tr.end_fill()
tr.color('black')
tr.penup()
tr.goto(0,30)
tr.pendown()
tr.width(8)
tr.goto(0,-10)
tr.color('red')
arc(0,-10,70,180,360)
tr.hideturtle()
tr.done()