import os
import sqlite3
import app
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from form import registerForm

instance_relative_config=True
#basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
#+ os.path.join(basedir, 'User.db')
app.config['SECRET_KEY'] = 'flaskExercise123'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    surname = db.Column(db.String(50))

app.app_context().push()

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/register')
def register():
    firstName = None
    surname = None
    form = registerForm()
    if form.validate_on_submit():
        firstName = form.firstName.data
        form.firstName.data = ''
        surname = form.surname.data
        form.surname.data = ''

    return render_template("register.html", firstName = firstName, surname = surname, form = form)

#Delete person

#Validate submission