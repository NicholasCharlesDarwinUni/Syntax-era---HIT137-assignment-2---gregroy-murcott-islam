import turtle 

t=turtle.Turtle()
s = turtle.Screen()



turtle.textinput('sides','sides please')

def draw_regular_polygon(t, sides, length):
    angle = 360 / sides
    
    for _ in range(sides):
        t.forward(length)
        t.right(angle)

draw_regular_polygon(t, 10, 100)

s.mainloop()