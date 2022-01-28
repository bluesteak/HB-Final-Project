"""Script to seed database."""

import os
import json
from datetime import datetime
from random import choice, randint

import model
import server
import seed_database
import crud


os.system("dropdb movies")
os.system("createdb movies")

model.connect_to_db(server.app)
model.db.create_all()

#Create a movie


movies_in_db = []
for n in range(5):
    movie_title = f"The Reverage of Deviled Egg - Movie {n}"
    poster = f"Poster film link {n}"


    db_movie = crud.create_movie(movie_title, poster)
    movies_in_db.append(db_movie)

model.db.session.add_all(movies_in_db)
model.db.session.commit()

# Create 5 users; each user will make 5 ratings
# for n in range(5):
#     email = f"moviecritic{n}@email.com"  
#     password = "123abc"

#     user = crud.create_user(email, password)
#     model.db.session.add(user)

#     # for _ in range(5):
#     #     random_movie = choice(movies_in_db)
#     #     score = randint(1, 5)

#     #     rating = crud.create_rating(user, random_movie, score)
#     #     model.db.session.add(rating)

# model.db.session.commit()


