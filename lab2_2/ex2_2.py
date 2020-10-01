import turtle as tr
import numpy as np
from random import *


def indeks(Ind):
	for i in Ind:
		numb(numbers_dict[i])


def numb(n):
	for angle, step in n[:-1]:
		tr.right(angle)
		tr.forward(step)
	last_angle, last_step = n[-1]
	tr.penup()
	tr.right(last_angle)
	tr.forward(last_step)
	tr.pendown()


tr.shape('turtle')
tr.color('blue')
n = 30
m = 10

with open('indeks_number.txt') as file:
	n0 = eval(file.readline())
	n1 = eval(file.readline())
	n2 = eval(file.readline())
	n3 = eval(file.readline())
	n4 = eval(file.readline())
	n5 = eval(file.readline())
	n6 = eval(file.readline())
	n7 = eval(file.readline())
	n8 = eval(file.readline())
	n9 = eval(file.readline())

numbers_dict = {0: n0, 1: n1, 2: n2, 3: n3, 4: n4, 5: n5, 6: n6, 7: n7, 8: n8, 9: n9}

indeks([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1])
tr.done()