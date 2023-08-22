# Movement and Speed of Ball
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.speed_of_ball = 0.1

    def move_right(self):
        # When left opponent misses the ball then turn starts with right
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def move_left(self):
        # When right opponent misses the ball then turn starts with left
        new_x = self.xcor() - self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        # Top and Bottom wall bounce
        self.y_move *= -1

    def bounce_x(self):
        # Left and Right paddle bounce
        self.x_move *= -1
        self.speed_of_ball *= 0.9

    def reset_position(self):
        # Resets to default position when a player misses ball
        self.goto(0, 0)
        self.speed_of_ball = 0.1
        self.bounce_x()
