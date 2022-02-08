"""CRUD operations."""

from model import db, User, Movie, Rating, Actor, Character, connect_to_db


def create_movie(movie_title,poster,overview):
    """Create and return a new movie."""

    movie = Movie(
        movie_title=movie_title,
        poster=poster,
        overview=overview
    )

    return movie

def create_character(char_name):
    """Create and return a character for a movie."""
    character = Character(char_name=char_name)

    return character
def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user

def create_actor(actor_name,gender,dob,other_name,biography,headshot):
    actor = Actor(
        actor_name=actor_name,
        gender=gender,
        dob=dob,
        other_name=other_name,
        biography=biography,
        headshot=headshot
    )
    return actor

def get_actor_by_id(actor_id):
    """Return a actor by primary key."""

    return Actor.query.get(actor_id)
# def create_rating(user, movie, score):
#     """Create and return a new rating."""

#     rating = Rating(user=user, movie=movie, score=score)

#     return rating



if __name__ == "__main__":
    from server import app

    connect_to_db(app)
