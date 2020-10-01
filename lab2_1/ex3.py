import turtle as tr
tr.shape("turtle")
def square(a):
    for i in range(4):
        tr.forward(a)
        tr.left(90)
square(50)
tr.done()