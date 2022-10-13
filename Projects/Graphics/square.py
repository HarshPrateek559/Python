"""
This is a simple program which uses the turtle library of Python to draw graphics. In this I have 
created a simple gray square on black background.
"""

from turtle import *

# This is the settings of the window. Screen() is the object that can change the attributes of the canvas
wn = Screen()
wn.setup(width=800, height=600)
wn.bgcolor("#000")

# We can make the canvas using the cv method of the window object.
canvas = wn.cv

# This is the way we can create the turtle object.
t = Turtle()
t.color('white') # This line change the color of the turtle and the line it draws
t.shape("turtle")
t.pensize(3) # It takes an integer and grow or shrink the size accordingly.
t.speed(1)  # It change the speed of the turtle, it takes an integer

# With the textinput method, we can take input in the canvas with the prompt
s = 100
#int(textinput("Square", "Enter the length of the edge"))

#int(input("Enter the length of the side of shape"))
t.fillcolor("darkgray")
# Drawing the square
t.begin_fill()
for i in range(4):
    
    t.forward(s)  # The forward command makes the turtle move forward while drawing the line. It takes a value which is the lenght of the line it is drawing

    t.left(90)  # The left command turns the turtle left by the specified no. of degree which it takes as argument.

t.end_fill()
Screen().exitonclick()