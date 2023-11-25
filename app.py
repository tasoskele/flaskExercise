from "" import _sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)
db = SQL("sqlite:///persons.db")

@app.route("/")
def index():
    return render_template("index.html")

#Delete person

#Validate submission