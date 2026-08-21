from flask import Flask, render_template, request
import random

app = Flask(__name__)

players = []
poem = []
players_remaining = []
game_started = False
game_finished = False
current_player = None


@app.route("/")
def home():
    return render_template(
        "index.html",
        players=players,
        game_started=game_started,
        current_player=current_player,
        game_finished=game_finished,
        message=message
    )


@app.route("/join", methods=["POST"])
def join():

    player_name = request.form["playerName"]

    message = ""

    if len(players) >= 10:
        message = "Maximum of 10 players allowed."

    elif player_name in players:
        message = "That nickname is already in use."

    else:
        players.append(player_name)

    return render_template(
        "index.html",
        players=players,
        game_started=game_started,
        game_finished=game_finished,
        message=message
    )


@app.route("/start", methods=["POST"])
def start():

    global game_started, current_player, players_remaining

    game_started = True
    players_remaining=players.copy()
    current_player=random.choice(players_remaining)
    players_remaining.remove(current_player) 

    print("Players:", players)
    print("Players Remaining:", players_remaining)
    print("Current Player:", current_player)

    return render_template(
        "index.html",
        players=players,
        game_started=game_started,
        current_player=current_player,
        poem=poem,
        game_finished=game_finished
    )

@app.route("/submit_line", methods=["POST"])
def submit_line():

    global current_player, game_finished

    line = request.form["poemLine"]

    poem.append(line)

    if players_remaining:
        current_player = random.choice(players_remaining)
        players_remaining.remove(current_player)

    else:
        game_finished = True
        current_player = None

    return render_template(
        "index.html",
        players=players,
        players_remaining=players_remaining,
        poem=poem,
        current_player=current_player,
        game_started=game_started,
        game_finished=game_finished
    )

@app.route("/new_game", methods=["POST"])
def new_game():

    global players
    global players_remaining
    global poem
    global current_player
    global game_started
    global game_finished

    players = []
    players_remaining = []
    poem = []
    current_player = None
    game_started = False
    game_finished = False

    return render_template(
        "index.html",
        players=players,
        players_remaining=players_remaining,
        poem=poem,
        current_player=current_player,
        game_started=game_started,
        game_finished=game_finished
    )


if __name__ == "__main__":
    app.run(debug=True)