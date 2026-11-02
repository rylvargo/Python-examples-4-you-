import turtle  # Imports the turtle graphics library

turtle.forward(100)  # Moves the turtle forward 100 pixels

turtle.done()  # Keeps the drawing window open


#--------------------------------------------------------------------------------------------------------------|
#  Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----|
#--------------------------------------------------------------------------------------------------------------|


import turtle  # Imports the turtle library

# Create a turtle
t = turtle.Turtle()

# Set turtle speed
t.speed(3)

# Draw a square
for i in range(4):
    t.forward(100)  # Move forward
    t.right(90)     # Turn right

# Change drawing color
t.color("red")

# Draw a circle
t.circle(50)

# Keep window open
turtle.done()