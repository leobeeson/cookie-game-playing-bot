# Game-Playing Bot: Cookie Clicker 

## Description
Automates UI actions for playing Cookie Clicker game, with the objective of maximizing `cookies per second` (CPS) produced.

## Behaviour
1. In `main.py`, experiment with different values for:
    * `game_duration`: How long you want the bot to play the game. 
        * Default = 300 seconds.
    * `check_interval`: How often do you want to check produced `cookies` (i.e. currency) and purchase available `cookie producers`. 
        * Default = 3 seconds.
2. Run `main.py` and find `Cookies per Second: $CPS` printed in the terminal after the end of `game_duration`.

## Requirements
1. Run `pip install -r requirements.txt` in terminal.
5. Run `python3 main.py` (or `python main.py` if on Windows with no Python2).

## Improvements
* Handle exceptions with the `WebDriverWait` class to improve execution flow.
* Improve expressiveness of typing `List[tuple]` to ~ list[tuple[WebElement, int]] (in Python >= 3.9).

## Caution:
### Game Page Brittleness: orteil.dashnet.org
* The webpage hosting the game is very often down (i.e. "This site can’t be reached. orteil.dashnet.org took too long to respond."), making playing the game, developing improvements, and testing improvements difficult.

## Credits:
- This project was motivated by the [Day 48 project](https://www.udemy.com/course/100-days-of-code/learn/lecture/21785294#questions/17098568), from the course [100 Days of Code: The Complete Python Pro Bootcamp for 2022](https://www.udemy.com/course/100-days-of-code/learn/).
