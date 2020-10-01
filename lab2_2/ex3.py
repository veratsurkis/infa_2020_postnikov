import turtle as tr
tr.shape('circle')
tr.forward(800)
tr.forward(-1100)
x = -300
y = 0
Vx = 10
Vy = 30
ay = -3
dt = 0.1
while Vx > 0.2:
	tr.goto(x, y)
	if y < 0:
		Vy = -0.7*Vy
		Vx = 0.8*Vx
	x += Vx*dt
	y += Vy*dt + ay*dt**2/2
	Vy += ay*dt
tr.done()