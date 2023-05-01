# US States Game
This is a simple, interactive U.S States Game that allows users to practice their knowledge of U.S state names. The program displays a blank map of the United States and prompts the user to enter the name of a state. When the user inputs a correct state name, the program will display the state name on the map at the appropriate location. The game continues until the user has correctly identified all 50 states or decides to exit the game by typing 'Exit'. Upon exiting, the program generates a CSV file called 'states_to_learn.csv', which lists the states that the user did not correctly identify.

![Capture](https://user-images.githubusercontent.com/83295029/235550086-4d4e9d27-8560-4171-805b-ec77347d350d.PNG)

## Getting Started!

These instructions will help you get the game up and running on your local machine.

### Prerequisites
Python 3.x or higher

Pandas

### Installation
To install pandas:

Inside the command prompt (Windows) or Terminal (Mac), enter the following;
```
pip install pandas
```
Clone the repository to your local machine:

```
git clone https://github.com/mlindens/US_States_Game.git
```
Navigate to the project directory:
```
cd US_States_Game
```
Run the game:
```
python main.py
```
### How to Play
* Enter the name of a state.
* Case-sensitive is not in effect, but correct spelling is.
* Type exit to close the game and the game will create a states_to_learn.csv file.
* States_to_learn.csv contains all states you failed to guess correctly.

### Built With
* [Python](http://www.python.org)
* [Pandas](https://pandas.pydata.org/)
* [Turtle graphics library](https://docs.python.org/3/library/turtle.html)
