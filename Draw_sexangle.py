#Draw_Sexangle.py
import turtle as t
t.setup(800,500,200,200)
t.penup()
t.goto(-100, -100)
t.pendown()
t.pensize(5)
t.color("red")
for i in range(6):
    t.fd(150)
    t.left(60)
