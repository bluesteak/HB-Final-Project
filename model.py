""" Models for Cannes Pineapple app. """

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQAlchemy()

class Movie(db.Model):
    """A movie."""

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

class Characters(db.Model):
    """Movie's character."""

    __tablename__ = "characters"

    char_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    char_name = db.Column(db.String)
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.movie_id"))
 


    movie = db.relationship("Movie", backref="characters")

    def __repr__(self):
        return f'<Characters char_id={self.char_id} >'
    

def connect_to_db(flask_app, db_uri="postgresql:///movies", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    connect_to_db(app)
