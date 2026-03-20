import turtle

# Create screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create turtle
pen = turtle.Turtle()
pen.color("red")
pen.fillcolor("red")
pen.speed(3)

# Draw heart
pen.begin_fill()

pen.left(140)
pen.forward(180)

pen.circle(-90, 200)
pen.left(120)
pen.circle(-90, 200)

pen.forward(180)

pen.end_fill()

# Move to write text
pen.penup()
pen.goto(0, -100)
pen.color("black")

# Write text
pen.write("Vansh", align="center", font=("Arial", 20, "bold"))

# Hide turtle
pen.hideturtle()

turtle.done()