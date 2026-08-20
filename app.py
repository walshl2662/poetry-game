from flask import Flask, render_template, request

app = Flask(__name__)
players = []

@app.route("/")
def home():
    return render_template("index.html", players=players)

@app.route("/join", methods=["POST"])
def join():

    player_name = request.form["playerName"]

    players.append(player_name)

    return render_template("index.html", players=players)

if __name__ == "__main__":
    app.run(debug=True)