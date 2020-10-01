import turtle as tr
import numpy as np

def polygon(a,n):
    tr.penup()
    tr.forward(a/(2*np.sin(np.pi/n)))
    tr.down()
    tr.left(90+180/n)
    for j in range(n):
        tr.forward(a)
        tr.left(360/n)
    tr.penup()
    tr.right(90+180/n)
    tr.backward(a/(2*np.sin(np.pi/n)))
    tr.pendown()
tr.shape("turtle")
tr.speed(3)
#polygon(100,3)
for i in range(3,13,1): 
	polygon(10*i,i)
tr.done()