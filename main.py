from os import system
from webbrowser import open

page = "http://localhost:5000"

try:
    from flask import Flask, render_template, redirect
    from pyTwistyScrambler import scrambler333
except:
    system("python -m pip install -r requirements.txt")
    from flask import Flask, render_template, redirect
    from pyTwistyScrambler import scrambler333
app = Flask(__name__)

@app.route("/")
def mainpage():
    return render_template("index.html")
    
@app.route("/full")
def scramble():
    try:
        scramble = scrambler333.get_WCA_scramble()
    except:
        scramble = "The reason you are seeing this message is that you don't have node js Installed, <a href='https://nodejs.org'>Click here</a>"
    return render_template("scramble.html", scramble=scramble)

@app.route("/f2l")
def scramble_f2l():
    try:
        scramble = scrambler333.get_F2L_scramble()
    except:
        scramble = "The reason you are seeing this message is that you don't have node js Installed, <a href='https://nodejs.org'>Click here</a>"
    return render_template("scramble.html", scramble=scramble)

@app.route("/ll")
def scramble_ll():
    try:
        scramble = scrambler333.get_LL_scramble()
    except:
        scramble = "The reason you are seeing this message is that you don't have node js Installed, <a href='https://nodejs.org'>Click here</a>"
    return render_template("scramble.html", scramble=scramble)

open(page)

app.run(port=5000, debug=True)