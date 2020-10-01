import turtle as tr

def spider(n,r): #r - Длина лапки
    tr.shape("turtle")
    for i in range(n):
        tr.forward(r)
        tr.stamp()
        tr.backward(r)
        tr.right(360/n)
spider(12,100)
tr.done()