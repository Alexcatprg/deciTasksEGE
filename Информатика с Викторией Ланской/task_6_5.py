from turtle import *
tracer(0)
left(90)
k = 20
right(90)
for i in range(3):
    pendown()
    for j in range(2):
        forward(10 * k)
        right(90)
        forward(10 * k)
        right(90)
    penup()
    forward(10 * k)
    right(90)
    forward(5 * k)
    right(90)
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(5)
done()