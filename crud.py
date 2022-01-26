"""CRUD operations."""

from model import db, Movie, Actors, connect_to_db


def create_actors(name):
    actor = Actors(
        name = name
    )

    return actor


if __name__ == "__main__":
    from server import app

    connect_to_db(app)
