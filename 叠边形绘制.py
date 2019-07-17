#Draw_叠边形.py
import turtle as t
t.setup(800, 500)
t.penup()
t.goto(-100,-100)
t.pendown()
t.pensize(5)
t.pencolor("green")
for i in range(9):
    t.fd(200)
    t.left(80)
