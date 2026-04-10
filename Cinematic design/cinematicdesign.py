import turtle
import colorsys

# Screen setup
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('silver')
t.speed(0)
t.hideturtle()

# Pattern parameters
n = 36  # Number of circles/shapes
h = 0

for i in range(200):
    # Colorsys diye vibrant color transition kora jay
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h += 1/n
    t.color(c)
    
    # Mathematical pattern creation
    t.left(145)
    t.forward(i * 2)
    t.circle(i, 100)
    
    # Thickness control
    t.pensize(i/100 + 1)

turtle.done()