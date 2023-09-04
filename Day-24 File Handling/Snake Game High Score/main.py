# ====== Welcome to the Snake Game High Score ===== #
# This snake game is different than the previous one.
# We have added all time high score in this game by using file handling concept.
# Controls: all four arrow keys for direction. 
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0)  # It is used to not track(display) all the activity step by step on screen.
# When we use screen.update() it tracks the final position after all the steps which are not tracked by screen.tracer(0)
# We must use screen.update() or it will display nothing.
# steps are nothing but the code written by us to make changes on the screen.

# Create, Expand and Give Direction to snake body
snake = Snake()
# Randomly create snake food on the screen
food = Food()
# Display score and Game Over on the screen
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_in_on = True
while game_in_on:
    screen.update()
    time.sleep(0.1)  # It is used to increase or decrease speed of snake.
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail.
    for segment in snake.segments[1:]:  # Slice in python
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
