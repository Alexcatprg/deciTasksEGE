from turtle import *
tracer(0)
left(90)
k = 40
for i in range(111):
    forward(123 * k)
    right(120)
pu()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(5)
done()
# Выдаёт угол (Наталье Фёдоровне)