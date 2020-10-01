from random import *
import turtle as tr


number_of_turtles = 15
steps_of_time_number = 300

tr.speed(0)
tr.width(3)
tr.penup()
tr.goto(300,300)
tr.pendown()
tr.goto(300,-300)
tr.goto(-300,-300)
tr.goto(-300,300)
tr.goto(300,300)
tr.hideturtle()


pool = [tr.Turtle(shape='circle') for i in range(number_of_turtles)]


i = 0
dx_dy_list = []
x_y_list = []
for unit in pool:
    unit.speed(0)
    unit.hideturtle()
    unit.penup()
    unit.turtlesize(0.5,0.5,0.5)
    dx, dy = randint(-10,10), randint(-10,10)
    x, y = randint(-299, 299), randint(-299, 299)
    dx_dy_list.append((dx, dy))
    x_y_list.append((x, y))
    unit.goto(x, y)
    unit.showturtle()
    i += 1

for k in range(steps_of_time_number):
    i = 0
    for unit in pool:
        unit.speed(0)
        dx, dy = dx_dy_list[i]
        x, y = x_y_list[i]
        if not -300 < x + dx < 300:
            dx = -dx
        if not -300 < y + dy < 300:
            dy = -dy
        unit.goto(x + dx, y + dy) 
        dx_dy_list[i] = dx, dy
        x_y_list[i] = x + dx, y + dy
        i += 1
