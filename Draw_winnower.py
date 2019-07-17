#Draw_winnoer.py
import turtle as t
t.setup(800, 500)
t.pensize(4)
for i in range(4):
    t.seth(270 * i)
    t.fd(150)
    t.right(90)
    t.circle(-150,45)
    t.goto(0,0)
