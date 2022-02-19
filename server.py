""" Server for Cannes Pineapple movie database app. """

from flask import Flask
from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db, db
from jinja2 import StrictUndefined 

import requests
import crud
import os

app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]

app.jinja_env.undefined = StrictUndefined

#HomePage
@app.route("/")
def homepage():
    """ Show homepage """
    return render_template("homepage.html")

@app.route("/movies")
def all_movies():
    """View all movies."""

    movies = crud.get_movies()
    return render_template("all_movies.html", movies=movies)

@app.route("/actors")
def all_actors():
    """View all Actors."""

    actors = crud.get_actors()
    return render_template("all_actors.html", actors=actors)


@app.route("/actors/<id>")
def actor_detail(id):
    actor = crud.get_actor_by_id(id)
    return render_template("actor_detail.html",actor=actor)

@app.route("/movies/<id>")
def movie_detail(id):
    movie = crud.get_movie_by_id(id)
    return render_template("movie_detail.html",movie=movie)

@app.route("/login", methods=["POST"])
def login():

    email = request.form.get("email")
    password = request.form.get("password")
    user = crud.get_user_by_email(email)
    #Check for correct email/password and flash message
    if not user or user.password != password:
        flash("Wrong email or password")
    #if correct, login user
    else: 
        session["user_email"] = user.email
        flash(f"Welcome Back, {user.email}!")
        
    return redirect("/")

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
