from turtle import *
pat = Turtle()
c = ['blue','green','red','yellow','orange','pink','purple']
bgcolor("black")
speed(30)
for i in range(9):
    for j in range(1,8,1):
        circle(10*j)
        color(c[i%6])
    right(200)

turtle.done()
