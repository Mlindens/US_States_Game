import turtle
import pandas

"""
This program is a game that allows users to practice their knowledge of U.S state names.

The program displays a blank map of the United States and prompts the user to enter the name of a state. 
When the user inputs a correct state name, 
the program will display the state name on the map at the appropriate location. 
The game continues until the user has correctly identified all 50 states or decides to exit the game by typing 'Exit'. 

Upon exiting, the program generates a CSV file called 'states_to_learn.csv', 
which lists the states that the user did not correctly identify.

Dependencies:
- turtle
- pandas

Variables:
- screen: The turtle screen where the map is displayed.
- image: The image file containing the blank map of the U.S.
- data: A pandas DataFrame containing the x and y coordinates of each state's label on the map.
- all_states: A list of all U.S state names.
- guessed_states: A list of correctly guessed state names.
- answer_state: The user's input for the state name.
- t: A turtle object used to draw the state names on the map.
- state_data: A pandas Series containing the x and y coordinates of the correctly guessed state.
"""

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    # Prompt user for state name input
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="Name a state").title()
    # Exit the game if the user types 'Exit'
    if answer_state == "Exit":
        # Create a list of states that the user did not guess
        missing_states = [state for state in all_states if state not in guessed_states]
        # Save the list of missing states to a CSV file
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # Check if the user's input is a valid state name
    if answer_state in all_states:
        # Add the state to the list of guessed states
        guessed_states.append(answer_state)
        # Create a turtle to display the state name on the map
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # Get the state's coordinates from the data
        state_data = data[data.state == answer_state]
        # Move the turtle to the state's coordinates and write the state name
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

