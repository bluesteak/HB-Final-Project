""" Server for Cannes Pineapple movie database app. """

from flask import Flask
from flask import (Flask, render_template, request, flash, session, redirect,url_for)
from flask import jsonify



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
    characters = crud.get_characters_from_actor(id)
    character = crud.get_character_by_actor_id(id)
    return render_template("actor_detail.html",actor=actor, character=character,characters=characters)


@app.route("/movies/<id>")
def movie_detail(id):
    movie = crud.get_movie_by_id(id)
    return render_template("movie_detail.html",movie=movie)


@app.route("/movies/<movie_id>/ratings", methods=["POST"])
def create_rating(movie_id):
    """Create a new rating for the movie."""

    logged_in_email = session.get("user_email")
    rating_score = request.form.get("rating")

    if logged_in_email is None:
        flash("You must log in to rate a movie.")
    elif not rating_score:
        flash("Error: you didn't select a score for your rating.")
    else:
        user = crud.get_user_by_email(logged_in_email)
        movie = crud.get_movie_by_id(movie_id)

        rating = crud.create_rating(user, movie, int(rating_score))
        db.session.add(rating)
        db.session.commit()

        flash(f"You rated this movie {rating_score} out of 5.")

    return redirect(f"/movies/{movie_id}")    

@app.route("/signup")
def register():
    """Show sign up page and term&conditions"""
    return render_template("register.html")

# @app.route("/signup", methods=["POST"])
# def register_user():
#     """Create a new user"""
#     name = request.form.get("name")
#     email = request.form.get("email")
#     password = request.form.get("password")
#     user = crud.get_user_by_email(email)
    
#     #Check if account exists, flash message for True
#     if user:
#         flash("Account already exists. Please try another email.")
#     #If False, create a new account
#     else:
#         user = crud.create_user(email, password, name)
#         flash("Congratulations! You account has been create. Please log in")
#     return redirect("/")

@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/login",methods=["POST"])
def login_user():
    """Process existing user login"""
    email = request.form.get("email")
    password = request.form.get("password")
    user = crud.get_user_by_email(email)

    if not user or user.password != password:
    #Wrong email and password
        flash("Wrong email or password. Please try again")


    else:
    #Log in user
        session["user_name"] = user.name
        session["user_email"] = user.email
        session["user_id"] = user.user_id

        flash(f"Welcome Back, {user.name}!")
    return redirect("/")


@app.route("/users")
def all_users():
    """View all users."""

    users = crud.get_users()

    return render_template("all_users.html", users=users)

@app.route("/users/<user_id>")
def show_user(user_id):
    """Show details on a particular user."""

    user = crud.get_user_by_id(user_id)

    return render_template("user_details.html", user=user)





@app.route("/logout")
def logout():
    """Log and and delete session"""
    del session["user_id"]

    flash("You've logged out!")
    return redirect("/")




if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
