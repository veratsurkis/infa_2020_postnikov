import turtle as tr
import numpy as np
from random import *


def indeks(Ind):
	for i in Ind:
		numb(numbers_dict[i])
tr.shape('turtle')
tr.color('blue')

def numb(n):
	for angle, step in n[:-1]:
		tr.right(angle)
		tr.forward(step)
	last_angle, last_step = n[-1]
	tr.penup()
	tr.right(last_angle)
	tr.forward(last_step)
	tr.pendown()


n = 30
m = 15

n0 = ((90, 2*n), (90, n), (90, 2*n), (90, n), (0, n+m)) #Значения для right, forward. Последний кортеж - с отрывом пера


n1 = ((-45, -np.sqrt(2)*n), (0, np.sqrt(2)*n), (-45, -2*n), (0, 2*n), (90, n+m))


n2 = ((0, -n), (0, n), (90, n), (45, np.sqrt(2)*n), (-135, n), (0, -n), (-45, np.sqrt(2)*n), (-45, n), (90, n+m))


n3 = ((0,-n), (0, n), (-45, -np.sqrt(2)*n), (45, n), (-45, -np.sqrt(2)*n), (0, np.sqrt(2)*n), (45, -n), (-45, np.sqrt(2)*n), (45, n+m)) 


n4 = ((-90, -2*n), (0, n), (-90, n), (90, n), (90, 2*n+m))


n5 = ((0, -n), (-90, -n), (-90, -n), (90, -n), (90, -n), (0, n), (-90, n), (-90, n), (90, n), (90, 2*n+m))


n6 = ((0, -n), (-90, -2*n), (-90, -n), (90, n), (-90,n), (90, n), (90, 2*n+m))


n7 = ((0, -n), (0, n), (-45, -np.sqrt(2)*n), (-45, -n), (0, n), (45, np.sqrt(2)*n), (45, n+m))


n8 = ((0, -n), (-90, -2*n), (-90, -n), (90, n), (-90, n), (0, -n), (90, n), (90, n+m))


n9 = ((0, -n), (-90, -n), (-90, -n), (-45, np.sqrt(2)*n), (0, -np.sqrt(2)*n), (135, n), (90, n+m))


numbers_dict = {0: n0, 1: n1, 2: n2, 3: n3, 4: n4, 5: n5, 6: n6, 7: n7, 8: n8, 9: n9}

indeks([1, 4, 1, 7, 0, 0])

tr.done()