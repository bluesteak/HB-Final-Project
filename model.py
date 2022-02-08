""" Models for Cannes Pineapple app. """

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Movie(db.Model):
    """"A movie."""
    __tablename__ = "movies"

    movie_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    movie_title = db.Column(db.String)
    genre = db.Column(db.String)
    poster = db.Column(db.String)
    watch_link = db.Column(db.String)
    overview = db.Column(db.Text)
    release_date = db.Column(db.DateTime)

    def __repr__(self):
        return f'<Movie movie_id={self.movie_id} title={self.movie_title}>'

class Character(db.Model):
    """"Movie's character."""
    __tablename__ = "characters"

    char_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    char_name = db.Column(db.String)
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.movie_id"))
    actor_id = db.Column(db.Integer, db.ForeignKey("actors.actor_id"))


    movie = db.relationship("Movie", backref="characters")
    actor = db.relationship("Actor",backref="characters")

    def __repr__(self):
        return f'<Character char_id={self.char_id} char_name={self.char_name}>'
 
    
class Actor(db.Model):

    __tablename__ = "actors"

    actor_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    actor_name = db.Column(db.String)
    gender = db.Column(db.String)
    dob = db.Column(db.DateTime)
    other_name = db.Column(db.String)
    ethnicity = db.Column(db.String)
    biography = db.Column(db.Text)
    headshot = db.Column(db.String)
    

    def __repr__(self):
        return f'<Actor actor_id={self.actor_id} actor_name={self.actor_name}>'

class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String)
    password = db.Column(db.String)

    # ratings = a list of Rating objects

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}>"

class Rating(db.Model):
    """A movie rating."""

    __tablename__ = "ratings"

    rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    score = db.Column(db.Integer)
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.movie_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    movie = db.relationship("Movie", backref="ratings")
    user = db.relationship("User", backref="ratings")

    def __repr__(self):
        return f"<Rating rating_id={self.rating_id} score={self.score}>"

def connect_to_db(flask_app, db_uri="postgresql:///movies", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)
    print("Connected to the database")

if __name__ == "__main__":
    from server import app
    connect_to_db(app)
