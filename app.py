import os
import markovify
from flask import Flask, render_template

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(basedir, "corpus.txt")) as f:
    corpus = f.read()

text_model = markovify.Text(corpus, state_size=3)

def make_post():
    output = ""
    for i in range(6):
        sentence = text_model.make_sentence(tries=100)
        output += sentence.strip() + " "
    return output


@app.route("/")
def hello():
    return render_template("index.html", text=make_post())
