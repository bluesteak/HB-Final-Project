from model import db, User, Movie, Rating, Actor, Character, Favorite, connect_to_db


def get_char(id):
    char = db.session.query(Character).options(db.joinedload('movie')).filter(Character.movie_id==id).all()
    return char


"""
***********************************
    USER SECTION - RATING/CREATE FAVORITE LIST
***********************************
"""   
def get_movie_by_user(id):
    movie_list = (db.session.query(Movie).join(Rating).filter(Rating.user_id==id).all())
    return movie_list
    
def get_fav_by_user(id):
    fav_list = (db.session.query(Movie).join(Favorite).filter(Favorite.user_id==id).all())
    return fav_list


def create_fav(user,movie):
    fav = Favorite(user=user,movie=movie)
    return fav


"""
***********************************
    MOVIE QUERY DETAIL - FOR HOMEPAGE
***********************************
"""   
def get_asian_lead():
    asian_lead = db.session.query(Character).options(db.joinedload('movie')).filter(Character.is_lead=="Yes").all()
    return asian_lead