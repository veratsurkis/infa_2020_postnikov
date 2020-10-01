import turtle as tr

tr.shape("turtle")
def square(a):
    for i in range(4):
        tr.forward(a)
        tr.left(90)

for j in range(1,11,1):
    n=20
    square(j*n)
    tr.penup()
    tr.backward(n/2)
    tr.right(90)
    tr.forward(n/2)
    tr.left(90)
    tr.pendown()
tr.done()