import pandas
import turtle
# creating out screen with the image as our shape
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
# reading and saving all the U.S. States data from the CSV file into a list
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
# creating a while loop for the user to guess the name of all the U.S. States with 50 chances.
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct",
                                    prompt="What's another state's name?").title()
    # if the user types in the word "exit", then a list of all the states than he missed will be created in a .CSV file called "states to learn"
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states to learn.csv")
        break
    # if statement to add the name of the state into the correct location in the screen if the user guess is correct.
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


screen.exitonclick()
