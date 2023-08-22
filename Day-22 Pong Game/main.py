# ====== Welcome to the Pong Game ====== #
# This is a two player game with controls given below.
# Player 1: w - Up, s - Down
# Player 2: PgUp - Up, PgDn - Down

from turtle import Screen  # from "filename" import "class_name"
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))  # Creating object for right paddle
l_paddle = Paddle((-350, 0))  # Creating object for left paddle
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.speed_of_ball)
    screen.update()
    ball.move_right()

    # Detect collision with wall i.e. Top and Bottom wall, so we consider only Y coordinates.
    # If ball reached limit of +ve or -ve Y coordinates then bounce.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    # If ball reached limit of +ve or -ve X coordinate and near to paddles then bounce.
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect right paddle misses
    if ball.xcor() > 420:
        ball.reset_position()
        scoreboard.l_point()

    # Detect left paddle misses
    if ball.xcor() < -420:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
