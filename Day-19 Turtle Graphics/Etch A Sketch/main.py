# ===== Draw by moving the line ===== #
# press w to move forward
# press s to move backward
# press a to turn left
# press d to turn right
# press c to erase drawing and reset the position

from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forward():
    timmy.forward(10)


def move_backwards():
    timmy.back(10)


def move_counter_clockwise():
    timmy.left(10)


def move_clockwise():
    timmy.right(10)


def clear():
    timmy.reset()
    timmy.clear()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backwards, "s")
screen.onkey(move_counter_clockwise, "a")
screen.onkey(move_clockwise, "d")
screen.onkey(clear, "c")
screen.exitonclick()
