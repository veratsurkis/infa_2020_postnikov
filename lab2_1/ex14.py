import turtle as tr
import numpy as np

tr.shape("turtle")
def star(n,r):
	tr.penup()
	tr.forward(r)
	tr.left(180-90/n)
	tr.pendown()	
	if (n % 2 == 1):
		for i in range(1,n+1,1):
			tr.forward(np.sqrt(2*r**2+2*np.cos(np.pi/n)*r**2))
			tr.left(180-180/n)
	else:
		for i in range(1,n+1,1): # Тем не менее, загадочным образом это не работает для n=p*2, где p - простое число
			tr.forward(np.sqrt(2*r**2+2*np.cos(np.pi/n)*r**2))
			tr.left(180-360/n)
	tr.penup()
	tr.right(180-90/n)
	tr.backward(r)
	tr.pendown()
tr.speed(2)
star(11,50)
star(5,200)
tr.hideturtle()
tr.done()