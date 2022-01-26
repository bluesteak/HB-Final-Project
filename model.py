""" Models for Cannes Pineapple app. """

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Movie(db.Model):
    """"A movie."""
    __tablename__ = "movies"

    movie_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    movie_title = db.Column(db.String)
    film_location = db.Column(db.String)
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

    def __repr__(self):
        return f'<Actor actor_id={self.actor_id} actor_name={self.actor_name}>'

def connect_to_db(flask_app, db_uri="postgresql:///actors", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)


if __name__ == "__main__":
    from server import app

    connect_to_db(app)
