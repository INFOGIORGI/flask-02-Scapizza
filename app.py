from flask import Flask,render_template
import random

app = Flask(__name__)

@app.route("/")
def index():
    nomi = ["Roberto","Alberto","Samuele","Francesco"]
    return render_template("index.html",titolo = "Homepage",nome = random.choice(nomi))

@app.route("/about")
def about():
    nomi = ["Roberto","Alberto","Samuele","Francesco"]
    return render_template("about.html",titolo = "About",nome = random.choice(nomi))

@app.route("/contact")
def contact():
    nomi = ["Roberto","Alberto","Samuele","Francesco"]
    return render_template("contact.html",titolo = "Contact",nome = random.choice(nomi))

app.run(debug=True)