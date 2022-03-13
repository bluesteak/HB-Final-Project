"""CRUD operations."""

from model import db, User, Movie, Rating, Actor, Character, Favorite, connect_to_db

"""
***********************************
MOVIE - CREATE/SEARCH
***********************************
"""

def create_movie(movie_title,poster,overview,tmdb_id,release_date,watch_link,genre,back_drop,vote_average):
    """Create and return a new movie."""
    movie = Movie(
        movie_title=movie_title,
        poster=poster,
        overview=overview,
        tmdb_id=tmdb_id,
        release_date=release_date,
        watch_link=watch_link,
        genre=genre,
        back_drop=back_drop,
        vote_average=vote_average
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

def create_actor(actor_name,gender,dob,other_name,biography,headshot,known_for,place_of_birth):
    actor = Actor(
        actor_name=actor_name,
        gender=gender,
        dob=dob,
        other_name=other_name,
        biography=biography,
        headshot=headshot,
        known_for=known_for,
        place_of_birth=place_of_birth
    )
    db.session.add(actor)
    db.session.commit()  
    return actor



def get_actor_by_id(id):
    """Return a actor by primary key."""
    return Actor.query.get(id)

def get_character_by_actor_id(actor_id):
    """Return a actor by primary key."""
    return Character.query.get(actor_id)

def get_movie_by_id(id):
    return Movie.query.get(id)

def get_movie_by_tmdb(tmdb_id):
    return Movie.query.filter_by(tmdb_id=str(tmdb_id)).first()

def get_tmdb_ids():
    list = Movie.query.with_entities(Movie.tmdb_id).all()
    tmdb_list = [tmdb_id for tmdb_id, in list]
    return tmdb_list

def get_movies():
    """Return all movies."""

    return Movie.query.all()

def get_actors():
    """Return all movies."""

    return Actor.query.all()

def get_characters_from_actor(id):
    """Return all characters by actor Id."""

    return Character.query.filter_by(actor_id=id)

def get_actor_by_movie(id):
    # character_list = (db.session.query(Movie).join(Character).filter(Character.movie_id==movie_id)).all())
    actor_list = (db.session.query(Actor).join(Character).filter(Character.movie_id==id).all())
    return actor_list



def update_actor(id):
    update = Actor.query.filter_by(id=id).first()
    #update.ethnicity = "Vietnamese"
    return update

def update_movie(tmdb_id):
    update = Movie.query.filter_by(tmdb_id=tmdb_id).first()
    return update

def update_char(id):
    update = Character.query.filter_by(id=id).first()
    return update
"""
***********************************
USER SECTION - CREATE/LOGIN
***********************************
"""

def create_user(email, password, name):
    """Return a new user."""

    user = User(email=email, password=password,name=name)
    db.session.add(user)
    db.session.commit()
    return user

def check_user(email,password):
    """ Check if user email or password is correct"""
    user = User.query.filter_by(email=email, password=password).first()

    #correct password
    if user:
        return True
    else:
        return False


def get_user_by_id(user_id):
    """Return a user by primary key."""

    return User.query.get(user_id)


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()

def get_users():
    """Return all users."""

    return User.query.all()







def create_rating(user,movie, score):
    rating = Rating(user=user,movie=movie,score=score)
    return rating


if __name__ == "__main__":
    from server import app

    connect_to_db(app)
