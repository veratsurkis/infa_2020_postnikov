import turtle as tr
import numpy as np

tr.shape("turtle")
def circle(x,y,r):
    tr.penup()
    tr.goto(r+x,y)
    tr.pendown()
    for i in range(361):
        tr.goto(x+r*np.cos(i*np.pi/180),y+r*np.sin(i*np.pi/180))
for j in range(40,131,10):
	for k in range(-1,3,2):
		circle(j*k,0,j)
tr.done()