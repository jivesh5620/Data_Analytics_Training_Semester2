import turtle

# Set up screen
screen = turtle.Screen()
screen.bgcolor("white")

pen = turtle.Turtle()
pen.pensize(5)

# Draw face
pen.fillcolor("yellow")
pen.begin_fill()
pen.circle(100)
pen.end_fill()

# Eyes
pen.penup()
pen.goto(-40, 120)
pen.pendown()
pen.fillcolor("black")
pen.begin_fill()
pen.circle(20)
pen.end_fill()

pen.penup()
pen.goto(40, 120)
pen.pendown()
pen.begin_fill()
pen.circle(20)
pen.end_fill()

# Smile
pen.penup()
pen.goto(-40, 85)
pen.setheading(-60)
pen.pendown()
pen.circle(50, 120)

turtle.done()