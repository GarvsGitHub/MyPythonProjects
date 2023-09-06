# ===== Welcome to the Guess the States Name Game ===== #
# Gameplay: Type the states name with correct spelling to score.
# Control: Type "Exit" to quit the game.
# The missed states will be listed on the console at the end.

import turtle
import pandas

# Create Screen
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)  # Only gif file is accepted
turtle.shape(image)

# Fetch csv file
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    # Create user input screen to take answers
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    # Game logic
    if answer_state == "Exit":
        missed_states = []
        for state in all_states:
            if state not in guessed_states:
                missed_states.append(state)
        print(f"These are the missing states below that you didn't guessed:\n {missed_states}")
        break

    if answer_state in all_states:
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            t.goto((int(state_data.x)), (int(state_data.y)))
            t.write(answer_state, align="center")

screen.exitonclick()
