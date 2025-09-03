# Python program to print complete Koch Curve.
from turtle import *
import turtle

t = turtle.Turtle

s_amount = turtle.textinput('Sides','Sides:')
l_amount = turtle.textinput('Length','Length')
d_amount = turtle.textinput('Layers', 'Fractal Layers:')

turtle.speed("fast")
turtle.shape("turtle")

def centreTurtle():
    penup()                     

    backward(int(l_amount) / 2)
    left(90)
    forward(int(l_amount) / 2)
    right(90)

    # Pull the pen down – drawing when moving.        
    pendown()           

def draw_regular_polygon(t, sides, length):
    angle = 360 / sides
    
    for _ in range(sides):
        t.forward(length)
        t.right(angle)

def pointyShape(lengthSide, levels):
    if levels == 0:
        forward(lengthSide)
        return
    lengthSide /= 3.0
    pointyShape(lengthSide, levels-1)
    right(60)
    pointyShape(lengthSide, levels-1)
    left(120)
    pointyShape(lengthSide, levels-1)
    right(60)
    pointyShape(lengthSide, levels-1)

def drawFrac(sides, length, depth):
    
    for i in range(int(sides)):    
        pointyShape(int(length), int(depth))
        right(360 / int(sides))

centreTurtle()

if (d_amount == 0):
    drawPoly(t, s_amount, l_amount)
else:
    drawFrac(s_amount, l_amount, d_amount)
          


    mainloop()  