#CalPiV2.py
from random import randint
from time import perf_counter
import turtle as t

t.penup()
t.pendown()
t.color("black",)
t.begin_fill()
for i in range(4):
    t.fd(200)
    t.left(90)
t.end_fill()
t.fd(100)
t.pencolor("green")
t.circle(100,360)
t.penup()

DARTS = 10000
hits = 0.0
start = perf_counter()
for i in range(1, DARTS+1):
    x, y = randint(0,200), randint(0,200)
    dist = pow( (x-100) ** 2 + (y-100) ** 2, 0.5)
    if dist <=100:
        hits += 1
        t.goto(x,y)
        t.dot(3,"white")
    else:
        t.goto(x,y)
        t.dot(3,"red")
pi = 4 * (hits/DARTS)
print("圆周率值是: {}".format(pi))
print("运行时间是: {:.5f}s".format(perf_counter() - start))
