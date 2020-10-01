import turtle as tr
import numpy as np

def spiral(n,step):
   a=0
   for i in range(n):
    tr.forward(a)
    tr.left(90)
    a=a+step
tr.shape("turtle")
tr.speed(3)
spiral(30,10)
tr.done()