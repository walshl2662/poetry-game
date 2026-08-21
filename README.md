# Poetry Game

## Overview

This assignment was submitted by Liam Walsh (24382679) as part of the Reassessment for the module Software Engineering (CSU22013), Trinity College Dublin.

## Brief

The assignment brief was as follows:

    Design and implement an app or website capable of supporting the construction of a poem by a group of players. The game should present an initial, randomly selected player to begin the poem construction. That player will write a line, and press return. The next randomly chosen player will be prompted to add a line, and so on. The emerging poem should be available to all players as it forms. The game should end when all players have had a turn. Note that your solution need not support multiple parallel teams. You may chose to develop a visual front end, or implement a very simple text based interface as you prefer. You may chose any architecture you deem appropriate. 

## Features

- Join a game with a nickanme
- Prevent duplicate nicknames
- Maximum of 10 players
- Random player selection
- One turn per player
- Shared poem displayed at the end
- New Game button to reset the application

## Technologies Used

- Python
- Flask
- HTML
- CSS

## How to Run

1. Clone the repository.

    git clone https://github.com/walshl2662/poetry-game.git

2. Create and activate a cirtual environment.

    cd poetry-game
    python3 -m venv venv
    source venv/bin/activate

3. Install Flask:

    pip install flask
    
4. Run the application

    python3 app.py

5. Open your browser and go to:

    http://127.0.0.1:5000

## In case of bugs

If you find any bugs, please email Liam at walshl26@tcd.ie 




