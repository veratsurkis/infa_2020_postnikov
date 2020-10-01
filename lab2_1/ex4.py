import turtle as tr
import numpy as np

tr.shape("turtle")
def circle(r):
    tr.penup()
    tr.goto(r,0)
    tr.pendown()
    for i in range(361):
        tr.goto(r*np.cos(i*np.pi/180),r*np.sin(i*np.pi/180))
circle(100)
tr.done()