from os import system
from webbrowser import open
from sys import argv

if len(argv) < 1:
    port = 5000
else:
    try:
        input_port = argv[1]
        port = int(input_port)
    except:
        print("Invalid input port, please input a valid port, the port have to be a number")
        quit()
page = f"http://localhost:{port}"

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

app.run(port=port, debug=True)