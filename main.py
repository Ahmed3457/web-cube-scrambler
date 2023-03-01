from os import system
try:
    from flask import Flask, render_template, redirect
    from pyTwistyScrambler import scrambler333
except:
    system("python -m pip3 install -r requirements.txt")
app = Flask(__name__)

@app.route("/")
def mainpage():
    return render_template("index.html")
    
@app.route("/full")
def scramble():
    scramble = scrambler333.get_WCA_scramble()
    return render_template("scramble.html", scramble=scramble)

@app.route("/f2l")
def scramble_f2l():
    scramble = scrambler333.get_F2L_scramble()
    return render_template("scramble.html", scramble=scramble)

@app.route("/ll")
def scramble_ll():
    scramble = scrambler333.get_LL_scramble()
    return render_template("scramble.html", scramble=scramble)
app.run(port=5000, debug=True)