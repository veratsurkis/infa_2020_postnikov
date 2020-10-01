import turtle as tr
import numpy as np

def spiral(n,step):
    a=0
    for i in range(n):
        for j in range(360):
            tr.goto(a*np.cos(j*np.pi/180), a*np.sin(j*np.pi/180))
            a=a+step
tr.shape("turtle")
tr.speed(0)
spiral(5,0.05)
tr.done()