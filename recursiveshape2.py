import turtle 

t=turtle.Turtle()
s = turtle.Screen()



s_amount = turtle.textinput('sides','how many sides will your shape have?')
l_amount = turtle.textinput('length','how long is your shape?')
d_amount = turtle.textinput('recursiveness', 'how much shoudl the shape reoccur')

def draw_regular_polygon(t, sides, length):
    angle = 360 / sides
    
    for _ in range(sides):
        t.forward(length)
        t.right(angle)

draw_regular_polygon(t, int(s_amount), int(l_amount))



s.mainloop()