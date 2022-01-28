"""CRUD operations."""

from model import db, User, Movie, Rating, Actor, connect_to_db


def create_movie(movie_title,poster):
    """Create and return a new movie."""

    movie = Movie(
        movie_title=movie_title,
        poster=poster
    )

    return movie

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user

# def create_rating(user, movie, score):
#     """Create and return a new rating."""

#     rating = Rating(user=user, movie=movie, score=score)

#     return rating



if __name__ == "__main__":
    from server import app

    connect_to_db(app)
