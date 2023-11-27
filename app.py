from flask import Flask, redirect, render_template, request, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length
from flask_bootstrap import Bootstrap5
from db import db, User


app = Flask(__name__)
Bootstrap5(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'flaskExercise123'

db.init_app(app)

with app.app_context():
    db.create_all()


class registerForm(FlaskForm):
    name = StringField('name', validators=[InputRequired(), Length(min=3, max=50)])
    surname = StringField('surname', validators=[InputRequired(), Length(min=3, max=50)])
    submit = SubmitField('register')

class editForm(FlaskForm):
    name = StringField('name', validators=[InputRequired(), Length(min=3,max=50)])
    surname = StringField('surname', validators=[InputRequired(), Length(min=3, max=50)])
    submit = SubmitField('Update')

#db = SQLAlchemy(app)
#app.app_context().push()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/users")
def users():
    users = User.query.all()

    return render_template("users.html", users=users)

@app.route("/edit")
def editingUsers():
    users = User.query.all()

    return render_template("edit.html", editingUsers=users)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = registerForm()

    if request.method == "POST":
        if form.validate_on_submit():
            newUser = User(name=request.form["name"], surname=request.form["surname"])
            db.session.add(newUser)
            db.session.commit()
            return redirect(url_for("users"))
        else:
            flash("Not valid data", "error")

    return render_template("register.html", form=form)

@app.route("/edit-user/<int:user_id>", methods=["GET", "POST"])
def user(user_id):
    form = editForm()

    if request.method == "POST":
        # TODO validate form
        user = User.query.get(user_id)
        user.name = request.form["name"]
        user.surname = request.form["surname"]

        db.session.commit()

        return redirect(url_for("users"))
        #return render_template("edit-user.html", user=user)
    else:
        user = User.query.get(user_id)
        
        return render_template("edit-user.html", form=form, user=user)

#@app.route("/delete")
#def deleteUser():
    if request.method == "DELETE":
        db.session.delete(User.query.get(user_id))
        db.session.commit()
        return redirect(url_for("users"))
#    users = User.query.all()
#
#    return render_template("delete.html", deleteUser=users)

    if request.method == "POST":
        if form.validate_on_submit():
            newUser = User(name=request.form["name"], surname=request.form["surname"])
            db.session.add(newUser)
            db.session.commit()
            return redirect(url_for("users"))
        else:
            flash("Not valid data", "error")

    return render_template("register.html", form=form)