# Hirst painting is drawn by the artist 'Damien Hirst' and that is why it is named after him.
# The painting was sold in 2008 auction for around $198 Million USD.
# In this code we will draw hirst painting using turtle graphics.

import turtle
from turtle import Turtle, Screen
import random

color_list = [(249, 233, 19), (199, 12, 31), (235, 151, 37), (34, 81, 190), (231, 229, 5), (49, 219, 54), (197, 68, 23),
              (34, 33, 154), (216, 13, 9), (245, 42, 160), (71, 8, 51), (15, 154, 16), (227, 18, 119), (227, 152, 8),
              (14, 208, 223), (62, 19, 8), (224, 140, 208), (245, 45, 17), (248, 11, 8), (10, 97, 61), (90, 76, 11),
              (54, 210, 228), (17, 17, 57), (238, 156, 219), (83, 75, 211), (75, 213, 162), (83, 234, 193),
              (250, 8, 14), (60, 232, 241), (3, 67, 41), (243, 165, 157), (175, 179, 228), (35, 243, 160), (9, 79, 113),
              (26, 50, 233)]


def move_forward():
    for _ in range(10):
        timmy.dot(21, random.choice(color_list))
        timmy.forward(55)


def position():
    x = -260
    y = -250
    for _ in range(11):
        timmy.goto(x, y)
        move_forward()
        y += 50


turtle.colormode(255)
timmy = Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
position()

screen = Screen()
screen.exitonclick()
