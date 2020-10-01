import turtle as tr
import numpy as np

tr.shape("turtle")
def arc(x,y,r,angle_1,angle_2):
    tr.penup()
    tr.goto(x+r*np.cos(angle_1*np.pi/180),y+r*np.sin(angle_1*np.pi/180))
    tr.pendown()
    for i in range(angle_1,angle_2+1,1):
        tr.goto(x+r*np.cos(i*np.pi/180),y+r*np.sin(i*np.pi/180))
r = 100
x_1 = -3*r 
for j in range(4):
	x_1 = x_1 + 6*r/4
	arc(x_1, 0, r, 0, 180)
	arc(x_1 + 3*r/4, 0, r/4, 180, 360)
tr.done()