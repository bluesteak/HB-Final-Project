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


@app.route("/actor_detail")
def actor_detail(actor_id):
 

 def show_movie(actor_id):
    """Show details on a particular movie."""

    actor = crud.get_actor_by_id(actor_id)
    return render_template("actor_detail.html",actor=actor)




if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
