import turtle as t
import pandas as pd

data = pd.read_csv("states_data.csv")
states = data.state.to_list()

screen = t.Screen()
screen.title("India State Game")
image = "India-state.gif"
screen.addshape(image)
t.shape(image)
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/29 states corrects",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_state = []
        for state in states:
            if state not in guessed_states:
                missing_state.append(state)
        new_data = pd.DataFrame(missing_state)
        new_data.to_csv("States_to_learn.csv")
        break
    if answer_state in states:
        guessed_states.append(answer_state)
        timmy = t.Turtle()
        timmy.hideturtle()
        timmy.penup()
        state_data = data[data.state == answer_state]
        timmy.goto(state_data.x.item(), state_data.y.item())
        timmy.write(answer_state)

