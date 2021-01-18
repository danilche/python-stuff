from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route('/rps')
def rps():
    game_options = { ("rock", "paper"): "Comp's rock is beaten by your mighty paper!",
	("rock", "scissors") : "Comp's rock annihilated your scissors!",
	("paper", "rock"): "Comp's paper kills your rock!",
	("paper", "scissors"): "Comp's paper dies from your sharp scissors!",
	("scissors", "paper"): "Comp's scissors kill your paper!",
	("scissors", "rock"): "Comp's scissors get beaten by your rock. You rock!"}
    
    choices = ["rock", "paper", "scissors"]
    comp_choice = choices[randint(0, 2)]
    
    username = request.args.get('username', '')
    player_choice = request.args.get('player_choice', '')
    
    if player_choice == '':
        msg = 'You did not choose wisely. Try again.'
    else:
        if comp_choice == player_choice:
            msg = "It's a tie! A beautiful cord! A lifesaving fastener!"
        else:
            msg = game_options[comp_choice, player_choice]

    return render_template("rps.html").format(username, msg)
    
if __name__ == "__main__":
    app.run(debug=True)