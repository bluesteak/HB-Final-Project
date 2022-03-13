""" Server for Cannes Pineapple movie database app. """

from flask import Flask
from flask import (Flask, render_template, request, flash, session, redirect,url_for)
from flask import jsonify


from model import connect_to_db, db, Movie, User
from jinja2 import StrictUndefined 

import requests
import crud
import os
import cruddetail

app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]

app.jinja_env.undefined = StrictUndefined

"""
*****************************************
HOMEPAGE SECTION
*****************************************
"""

#HomePage
@app.route("/")
def homepage():
    """ Show homepage """
    asian_lead_movies = cruddetail.get_asian_lead()
    return render_template("homepage.html",asian_lead_movies=asian_lead_movies)


# @app.route("/giveme")
# def random():
#     movie = Movie.query.get(2)
#     return jsonify({"movie_title":movie.movie_title})

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

"""
***********************************
ACTOR SECTION
***********************************
"""

@app.route("/actors/<id>")
def actor_detail(id):
    actor = crud.get_actor_by_id(id)
    characters = crud.get_characters_from_actor(id)
    character = crud.get_character_by_actor_id(id)
    return render_template("actor_detail.html",actor=actor, character=character,characters=characters)


"""
***********************************
MOVIE SECTION
***********************************
"""

@app.route("/movies/<id>")
def movie_detail(id):
    movie = crud.get_movie_by_id(id)

    character = cruddetail.get_char(id)
    
    return render_template("movie_detail.html",movie=movie,character=character)

"""
***********************************
RATING
***********************************
"""

@app.route("/movies/<movie_id>/ratings", methods=["POST"])
def create_rating(movie_id):
    """Create a new rating for the movie."""

    logged_in_email = session.get("user")
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

"""
***********************************
REGISTER ACCOUNT SECTION
***********************************
"""

@app.route("/register")
def register():
    """Show sign up page and term&conditions"""
    return render_template("register.html")

# @app.route("/register", methods=['POST'])
# def signup():

#     email = request.form.get("email")
#     password = request.form.get("password")
#     name = request.form.get("name")
#     user = crud.create_user(email, password, name)
#     flash("Congratulations! You account has been create. Please log in")
#     return redirect("/")

@app.route("/register", methods=["POST"])
def register_user():
    """Create a new user"""
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    user = crud.get_user_by_email(email)
    
    #Check if account exists, flash message for True
    if user:
        flash("Account already exists. Please try another email.")
        return redirect("/signup")
    #If False, create a new account
    if not user:
        user = crud.create_user(email, password, name)
        flash("Congratulations! You account has been create. Please log in")
    return redirect("/")

"""
***********************************
LOG IN SECTION
***********************************
"""

@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/login",methods=["POST", "GET"])
def login_user():
    """Process existing user login"""
    email = request.form.get("email")
    password = request.form.get("password")
    user = crud.get_user_by_email(email)

    if not user or user.password != password:
    #Wrong email and password
        flash("Wrong email or password. Please try again")
        return redirect("/login")

    else:
    #Log in user
        session["user_name"] = user.name
        session["user"] = user.email
        # session["user_email"] = user.email
        session["user_id"] = user.user_id
        flash(f"Welcome Back, {user.name}!")
    return redirect(url_for("user"))

# @app.route("/users")
# def all_users():
#     """View all users."""

#     users = crud.get_users()

#     return render_template("all_users.html", users=users)

"""
***********************************
USER ROUTE SECTION
***********************************
"""

@app.route("/user", methods = ["POST", "GET"])
def user():
    if "user" in session:
        user = session["user"]
        current_user = crud.get_user_by_email(user)
        movie_list = cruddetail.get_movie_by_user(current_user.user_id)
        favorite_list = cruddetail.get_fav_by_user(current_user.user_id)
        current_password = current_user.password
        new_password = request.form.get("newpassword")
        if request.method == "POST":
            if current_user.password == request.form.get("currentpassword"):
                current_user.password = request.form.get("newpassword")
                db.session.commit()
                flash("Updated password!")
            else:
                flash("Incorrect current password. Please try again")
        

        return render_template("user_details.html",current_user=current_user,movie_list=movie_list,favorite_list=favorite_list)
    else:
        flash(f"Please login to view your account!")
        return redirect(url_for("login"))
    # """Show details on a particular user."""
    # show_user = crud.get_user_by_email(usr)
  
# ADD FAVORITE MOVIE
@app.route("/movies/<movie_id>/favorite", methods=["POST"])
def create_favorite(movie_id):
    """Create a new rating for the movie."""
    logged_in_email = session.get("user")
    adding = request.form.get("fav")

    if logged_in_email is None:
        flash("You must log in to add to favorite.")
    else:
        user = crud.get_user_by_email(logged_in_email)
        movie = crud.get_movie_by_id(movie_id)

        favorite = cruddetail.create_fav(user, movie)
        db.session.add(favorite)
        db.session.commit()

        flash(f"You have added this movie to your favorite list.")

    return redirect(f"/movies/{movie_id}")  



"""
***********************************
LOG OUT SECTION
***********************************
"""

@app.route("/logout")
def logout():
    """Log and and delete session"""
    del session["user_id"]

    flash("You've logged out!")
    return redirect("/")


"""
***********************************
SEARCH SECTION
***********************************
"""

@app.route("/search")
def search():
    q = request.args.get('q')
    if q:
        movies = Movie.query.filter(Movie.movie_title.contains(q.title()))
    else:
        movies = Movie.query.all()

    print(movies)
    return render_template("search_result.html", movies=movies)


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
