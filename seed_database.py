"""Script to seed database."""

import os
import json
import requests
from datetime import datetime

from random import random, choice, randint

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
person_list = ["1663195","21045","60851","1360317","127451","1625558","1489211","1620","206444","86633","232499","83586","68842","18307","11152"]

#kelly 
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
    db_actor = crud.create_actor(actor_name=response["name"],dob=response["birthday"],gender=response["gender"],other_name=response["also_known_as"],biography=response["biography"],headshot=response["profile_path"],known_for=response["known_for_department"],place_of_birth=response["place_of_birth"])
  
    #Get movie detail
    movie_find = f"https://api.themoviedb.org/3/person/{person}/movie_credits?api_key={api_key}&language=en-US"
    response_movie = requests.get(movie_find)
    response_movie = response_movie.json()
    movie_list = response_movie["cast"]
    #Add movie to database
    for num in range(len(movie_list)):
        movie_dict = movie_list[num]
        release_date = (movie_dict.get('release_date'))
        if release_date == "":
            release_date = None
        else:
            poster_base_url = "https://image.tmdb.org/t/p/original"

            tmdb_id = (movie_dict.get('id'))
            poster = (movie_dict.get('poster_path'))
            overview = (movie_dict.get('overview'))
            genre = (movie_dict.get('genres_id'))
            movie_title = (movie_dict.get('title'))
            back_drop = (movie_dict.get('backdrop_path'))
            vote_average=(movie_dict.get('vote_average'))
            char_name = (movie_dict.get('character'))
            movie = crud.get_movie_by_tmdb(movie_dict["id"])
            print(movie_title, release_date)
            if movie:
                db_character = crud.create_character(char_name=char_name,actor=db_actor,movie=movie)
            else:
                db_movie = crud.create_movie(tmdb_id=tmdb_id,movie_title=movie_title,poster=poster,overview=overview,watch_link="",genre=genre,release_date=release_date,back_drop=back_drop,vote_average=vote_average)
                print("Create movie",db_movie)

                db_character = crud.create_character(char_name=char_name,actor=db_actor,movie= db_movie)
#             movie = crud.get_movie_by_tmdb(response_movie["cast"][num]["id"])
#             if movie:
#                 db_character = crud.create_character(char_name=response_movie["cast"][num]["character"], actor=db_actor, movie=movie)
#             else:
#                 db_movie = crud.create_movie(tmdb_id=response_movie["cast"][num]["id"],movie_title=response_movie["cast"][num]["original_title"],poster=(poster_base_url+response_movie["cast"][num]["poster_path"]),overview=response_movie["cast"][num]["overview"],release_date=response_movie["cast"][num]["release_date"],watch_link="",genre=response_movie["cast"][num]["genre_ids"])
#                 print("Add movie to db",db_movie)

#                 db_character = crud.create_character(char_name=response_movie["cast"][num]["character"],actor=db_actor,movie=db_movie)

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


