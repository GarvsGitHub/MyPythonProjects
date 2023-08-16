# This code draws Triangle, Square, Pentagon, Hexagon, Heptagon, Octagon and Nonagon
# All the shapes drawn in different color.

from turtle import Turtle, Screen
from random import choice

tim = Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"
           ]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 10):
    tim.color(choice(colours))
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()
