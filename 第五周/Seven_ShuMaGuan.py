import turtle
def drawGap():          #绘制数码管间隔
    turtle.penup()
    turtle.fd(5)
def drawLine(draw):         #绘制单段数码管
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)
def drawDigit(dight):       #根据数字绘制七段数码管
    # 线段从 1 到 7 线段
    drawLine(True) if dight in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if dight in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if dight in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if dight in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if dight in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if dight in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if dight in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawData(data):         #获取要输出的数字
    for i in data:
        drawDigit(eval(i))     #通过eval（）函数将数字字符变为整数
def main():
    turtle.setup(800, 500, 200, 200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawData('20181010')
    turtle.hideturtle()
    turtle.done()
main()
