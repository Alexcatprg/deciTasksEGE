from turtle import *
tracer(0)
left(90)
k = 40
for i in range(24):
    forward(3 * k)
    left(60)
pu()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(5)
done()        