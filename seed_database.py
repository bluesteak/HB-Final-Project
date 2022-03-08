"""Script to seed database."""

import os
import json
import requests
from datetime import datetime
from random import choice, randint

import model
import server
import crud
import pdb

API = os.environ["TMDB_KEY"]
api_key = API
os.system("dropdb movies")
os.system("createdb movies")
model.connect_to_db(server.app)
model.db.create_all()

#The list of TMDB id for actor
person_list = ["2782707","1652045"]
#kelly "1663195"
#Actor Data
for person in person_list:
    print("Searching for person",person)
    actor_find = f"https://api.themoviedb.org/3/person/{person}?api_key={api_key}&language=en-US"
    
    response = requests.get(actor_find)
    response = response.json()
    


    # Get full image link and size for profile picture
    image_base_url = "https://image.tmdb.org/t/p/original"
    profile_url = image_base_url + response["profile_path"]
    response["profile_path"] = profile_url
        
    #Add actor to database
    profile_url = response["profile_path"]
    db_actor = crud.create_actor(actor_name=response["name"],dob=response["birthday"],gender=response["gender"],other_name=response["also_known_as"],biography=response["biography"],headshot=response["profile_path"])
  
    #Get movie detail
    movie_find = f"https://api.themoviedb.org/3/person/{person}/movie_credits?api_key={api_key}&language=en-US"
    response_movie = requests.get(movie_find)
    response_movie = response_movie.json()
       
    #Add movie to database
    for num in range(len(response_movie["cast"])):
        poster_base_url = "https://image.tmdb.org/t/p/original"
        # movie_list = []
        print("Here is the tmdb id:")
        print(response_movie["cast"][num]["id"])
        movie = crud.get_movie_by_tmdb(response_movie["cast"][num]["id"])
        if movie:
                db_character = crud.create_character(char_name=response_movie["cast"][num]["character"], actor=db_actor, movie=movie)
        else:
                db_movie = crud.create_movie(tmdb_id=response_movie["cast"][num]["id"],movie_title=response_movie["cast"][num]["original_title"],poster=(poster_base_url+response_movie["cast"][num]["poster_path"]),overview=response_movie["cast"][num]["overview"],release_date=response_movie["cast"][num]["release_date"],watch_link="")
                print("Add movie to db",db_movie)

                db_character = crud.create_character(char_name=response_movie["cast"][num]["character"],actor=db_actor,movie=db_movie)

#Adding missing data to Actor Database
# id_list = [1,2]
# for id in id_list:
#         crud.updateActor(id).ethnicity = "Vietnamese"
#         model.db.session.commit()

#Create test users:
for n in range(3):
        email = f"user{n}@test.com"  # Voila! A unique email!
        password = f"Testing{n}"
        name = f"Pineapple{n}"

        user = crud.create_user(email, password, name)
        model.db.session.add(user)
        print("add user to db",user)

        for i in range(5):
                random_movie = crud.get_movie_by_id(i)
                score = 5

                rating = crud.create_rating(user, random_movie, score)
                model.db.session.add(rating)
        
        model.db.session.commit()



