from turtle import *
tracer(0)
left(90)
k = 40
for i in range(4):
    forward(20 * k)
    right(270)
pu()
forward(6 * k)
right(270)
forward(10 * k)
right(90)
for l in range(2):
    forward(20 * k)
    right(270)
    forward(24 * k)
    right(270)
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(5)
done()    