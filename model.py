""" Models for Cannes Pineapple app. """

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Movie(db.Model):
    """"A movie."""
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True)
    movie_title = db.Column(db.String)
    genre = db.Column(db.String)
    poster = db.Column(db.String)
    watch_link = db.Column(db.String)
    overview = db.Column(db.Text)
    release_date = db.Column(db.DateTime)
    tmdb_id = db.Column(db.String)
    def __repr__(self):
        return f'<Movie id={self.id} title={self.movie_title}>'
    
class Actor(db.Model):

    __tablename__ = "actors"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    actor_name = db.Column(db.String)
    gender = db.Column(db.Integer)
    dob = db.Column(db.DateTime)
    other_name = db.Column(db.String)
    ethnicity = db.Column(db.String)
    biography = db.Column(db.Text)
    headshot = db.Column(db.String)

    
    def __repr__(self):
        return f'<Actor id={self.id} actor_name={self.actor_name}>'

class Character(db.Model):
    """"Movie's character."""
    __tablename__ = "characters"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    char_name = db.Column(db.String)
    is_lead = db.Column(db.String)
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.id"))
    actor_id = db.Column(db.Integer, db.ForeignKey("actors.id"))

    movie = db.relationship("Movie", backref="characters")
    actor = db.relationship("Actor",backref="characters")

    def __repr__(self):
        return f'<Character id={self.id} char_name={self.char_name} movie={self.movie} actor={self.actor}>'

class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String(50))
    name = db.Column(db.String(20))


    def __repr__(self):
        return f"<User user_id={self.user_id} name ={self.name} email={self.email}>"

class Rating(db.Model):
    """A movie rating."""

    __tablename__ = "ratings"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    score = db.Column(db.Integer)
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    movie = db.relationship("Movie", backref="ratings")
    user = db.relationship("User", backref="ratings")

    def __repr__(self):
        return f"<Rating rating_id={self.rating_id} score={self.score}>"

class Favorite(db.Model):
    """Favorite movie by user"""

    __tablename__ = "favorites"

    fav_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    movie = db.relationship("Movie", backref="favorites")
    user = db.relationship("User", backref="favorites")

    def __repr__(self):
        return f"<Favorite fav_id={self.fav_id}>"

def connect_to_db(flask_app, db_uri="postgresql:///movies", echo=False):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)
    print("Connected to the database")

if __name__ == "__main__":
    from server import app
    connect_to_db(app)
