from model import db, User, Movie, Rating, Actor, Character, connect_to_db


def get_char(id):
    char = db.session.query(Character).options(db.joinedload('movie')).filter(Character.movie_id==id).all()
    return char

