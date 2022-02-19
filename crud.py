"""CRUD operations."""

from model import db, User, Movie, Rating, Actor, Character, connect_to_db


def create_movie(movie_title,poster,overview,tmdb_id):
    """Create and return a new movie."""
    movie = Movie(
        movie_title=movie_title,
        poster=poster,
        overview=overview,
        tmdb_id=tmdb_id
    )
    db.session.add(movie)
    db.session.commit()
    return movie
   
            
#get movie_id
#create character from movie_id
def create_character(char_name,actor,movie):
    """Create and return a character for a movie."""
    character = Character(char_name=char_name,actor=actor,movie=movie)
    db.session.add(character)
    print("Adding character",character)
    db.session.commit()
    return character

def create_actor(actor_name,gender,dob,other_name,biography,headshot):
    actor = Actor(
        actor_name=actor_name,
        gender=gender,
        dob=dob,
        other_name=other_name,
        biography=biography,
        headshot=headshot
    )
    db.session.add(actor)
    db.session.commit()  
    return actor

def get_actor_by_id(id):
    """Return a actor by primary key."""
    return Actor.query.get(id)

def get_movie_by_id(id):
    return Movie.query.get(id)

def get_movie_by_tmdb(tmdb_id):
    return Movie.query.filter_by(tmdb_id=str(tmdb_id)).first()

def get_movies():
    """Return all movies."""

    return Movie.query.all()

def get_actors():
    """Return all movies."""

    return Actor.query.all()


def create_user(email, password):
    """Return a new user."""

    user = User(email=email, password=password)

    return user


def create_rating(user, movie, score):
    """Return a new rating."""

    rating = Rating(user=user, movie=movie, score=score)

    return rating
# def create_rating(user, movie, score):
#     """Create and return a new rating."""

#     rating = Rating(user=user, movie=movie, score=score)

#     return rating



if __name__ == "__main__":
    from server import app

    connect_to_db(app)
