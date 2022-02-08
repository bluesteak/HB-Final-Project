"""Script to seed database."""

import os
import json
import requests
from datetime import datetime
from random import choice, randint

import model
import server
import seed_database
import crud
api_key = "ca04f28350cde67bc24470dfe961b3dd"

os.system("dropdb movies")
os.system("createdb movies")
model.connect_to_db(server.app)
model.db.create_all()

#The list of TMDB id for actor
person_id = "1663195"
#Actor Data
actor_find = f"https://api.themoviedb.org/3/person/{person_id}?api_key={api_key}&language=en-US"
response = requests.get(actor_find)
response = response.json()
    
#Create json file to view
with open("actorslist.json","w") as f:
    json.dump(response, f, indent=4)

# Get full image link and size for profile picture
image_base_url = "https://image.tmdb.org/t/p/w45"
profile_url = image_base_url + response["profile_path"]
response["profile_path"] = profile_url

# Seed actor database to database
db_actor = crud.create_actor(actor_name=response["name"],gender=str(response["gender"]),dob=response["birthday"],other_name=response["also_known_as"][0],biography=response["biography"],headshot=response["profile_path"])
model.db.session.add(db_actor)
model.db.session.commit()

#Create a movie

movie_find = f"https://api.themoviedb.org/3/person/{person_id}/movie_credits?api_key={api_key}&language=en-US"

response_movie = requests.get(movie_find)
response_movie = response_movie.json()
    
#Create json file to view
with open("movielist.json","w") as f:
    json.dump(response_movie, f, indent=4)

for num in range(len(response_movie["cast"])):
    db_movie = crud.create_movie(movie_title=response_movie["cast"][num]["original_title"],poster=response_movie["cast"][num]["poster_path"],overview=response_movie["cast"][num]["overview"])
    model.db.session.add(db_movie)
    model.db.session.commit()


#Create a character
for num in range(len(response_movie["cast"])):
    db_character = crud.create_character(char_name=response_movie["cast"][num]["character"])
    model.db.session.add(db_character)
    model.db.session.commit()


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


#Actor Dummy Data
# with open("actor.json") as f:
#     actor_data = json.loads(f.read())
# actors_in_db = []

#Create a movie


# movies_in_db = []

# #Movie dummy data
# for n in range(5):
#     movie_title = f"The Reverage of Deviled Egg - Movie {n}"
#     poster = "https://www.whichwich.com/wp-content/uploads/2018/03/Egg.png"
#     genre = f"Action"
#     watch_link = f"Link {n}"
#     overview = "Here is the overview of the movie"
#     release_date = "01/01/1992"


#     db_movie = crud.create_movie(movie_title, poster,genre, watch_link,overview,release_date)
#     movies_in_db.append(db_movie)

# model.db.session.add_all(movies_in_db)
# model.db.session.commit()
# #Character Dummy Data
# for n in range(5):
#     char_name = f"Character {n}"
