from flask import Flask, render_template, request
import random

app = Flask(__name__)

players = []
poem = []
players_remaining = [] # initialises lists 
game_started = False
game_finished = False
current_player = None  # initialises game states


@app.route("/")
def home():
    return render_template(
        "index.html",
        players=players,
        game_started=game_started,
        current_player=current_player,
        game_finished=game_finished,
        message=""
    )


@app.route("/join", methods=["POST"])
def join():

    player_name = request.form["playerName"]

    message = ""

    if len(players) >= 10: # limits number of players
        message = "Maximum of 10 players allowed."

    elif player_name in players: # forbids duplicate nicknames
        message = "That nickname is already in use. Please choose another one"

    else:
        players.append(player_name) # adds player name to list

    return render_template(
        "index.html",
        players=players,
        game_started=game_started,
        game_finished=game_finished,
        message=message # returns game states
    )


@app.route("/start", methods=["POST"])
def start():

    global game_started, current_player, players_remaining

    game_started = True # begins game after entering all names
    players_remaining=players.copy() 
    current_player=random.choice(players_remaining) # randomly select one player
    players_remaining.remove(current_player) # removes selected player from list, cannot be chosen again

    print("Players:", players)
    print("Players Remaining:", players_remaining)
    print("Current Player:", current_player) # testing in terminal

    return render_template(
        "index.html",
        players=players,
        game_started=game_started,
        current_player=current_player,
        poem=poem,
        game_finished=game_finished # returns game states
    )

@app.route("/submit_line", methods=["POST"])
def submit_line():

    global current_player, game_finished

    line = request.form["poemLine"]

    poem.append(line) # adds line to poem list

    if players_remaining:
        current_player = random.choice(players_remaining)
        players_remaining.remove(current_player) # moves to next player if there is one

    else:
        game_finished = True
        current_player = None # finishes the game if everyone has taken their turn

    return render_template(
        "index.html",
        players=players,
        players_remaining=players_remaining,
        poem=poem,
        current_player=current_player,
        game_started=game_started,
        game_finished=game_finished # returns game states
    )

@app.route("/new_game", methods=["POST"])
def new_game(): # resets the game

    global players
    global players_remaining
    global poem
    global current_player
    global game_started
    global game_finished

    players = []
    players_remaining = []
    poem = [] # reinitialises all lists as empty
    current_player = None
    game_started = False
    game_finished = False # resets all game states to beginning

    return render_template(
        "index.html",
        players=players,
        players_remaining=players_remaining,
        poem=poem,
        current_player=current_player,
        game_started=game_started,
        game_finished=game_finished # returns game states
    )


if __name__ == "__main__":
    app.run(debug=True)