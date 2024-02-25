from turtle import *
tracer(0)
left(90)
k = 40
for i in range(4):
    right(90)
    forward(120 * k)
    right(90)
    forward(14 * k)
pu()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(5)
done()
# Выдаёт угол