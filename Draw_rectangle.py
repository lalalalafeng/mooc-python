#PythonDraw_rectangle.py
import turtle
turtle.setup(800, 800, 200, 200)
turtle.penup()
turtle.goto(-125,-125)
turtle.pendown()
turtle.pensize(20)
turtle.pencolor("blue")
for i in range(4):
    turtle.fd(150)
    turtle.left(90)
