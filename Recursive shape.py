import turtle

def draw_koch_edge(length, depth):
    
    if depth == 0:
        turtle.forward(length)
    else:
        segment = length / 3
        draw_koch_edge(segment, depth - 1)
        turtle.left(60)
        draw_koch_edge(segment, depth - 1)
        turtle.right(120)
        draw_koch_edge(segment, depth - 1)
        turtle.left(60)
        draw_koch_edge(segment, depth - 1)


def draw_geometric_pattern(sides, side_length, depth):
    
    angle = 360 / sides
    for _ in range(sides):
        draw_koch_edge(side_length, depth)
        turtle.right(angle)


def main():
    print("Welcome to the Geometric Pattern Generator!")
    print("This program draws a recursive geometric pattern using turtle graphics.")
    print("You can choose the number of sides, the length of each side, and the recursion depth.")
    
    # Get user input
    sides = int(input("Enter the number of sides for the polygon (e.g., 3 for triangle): "))
    side_length = int(input("Enter the length of each side in pixels (e.g., 300): "))
    depth = int(input("Enter the recursion depth (e.g., 3): "))

    # Setup turtle
    turtle.speed(0)
    turtle.bgcolor("white")
    turtle.color("blue")
    turtle.pensize(2)

    # Center the drawing
    turtle.penup()
    turtle.goto(-side_length // 2, side_length // 3)
    turtle.pendown()

    # Draw the pattern
    draw_geometric_pattern(sides, side_length, depth)

    print
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
