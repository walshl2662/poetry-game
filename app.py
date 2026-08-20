from flask import Flask, render_template, request
import random

app = Flask(__name__)

players = []
poem = []
players_remaining = []
game_started = False
current_player = None


@app.route("/")
def home():
    return render_template(
        "index.html",
        players=players,
        game_started=game_started,
        current_player=current_player
    )


@app.route("/join", methods=["POST"])
def join():

    player_name = request.form["playerName"]

    players.append(player_name)

    return render_template(
        "index.html",
        players=players,
        game_started=game_started
    )


@app.route("/start", methods=["POST"])
def start():

    global game_started, current_player, players_remaining

    game_started = True
    players_remaining=players.copy()
    current_player=random.choice(players_remaining)
    players_remaining.remove(current_player) 

    print(players)
    print(players_remaining)
    print(current_player)

    return render_template(
        "index.html",
        players=players,
        game_started=game_started,
        current_player=current_player
    )


if __name__ == "__main__":
    app.run(debug=True)