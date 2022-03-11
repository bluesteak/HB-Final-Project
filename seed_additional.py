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
model.connect_to_db(server.app)

person_list=["123"]
#Seed ethnicity
# id_list =[1,2]
# for id in id_list:
#     crud.updateActor(1).ethnicity = "Vietnamese"
# model.db.session.commit()

tmdb_list = crud.get_tmdb_ids()

# result = SomeModel.query.with_entities(SomeModel.col1, SomeModel.col2)
for tmdb in tmdb_list:
    trailer_find = f"https://api.themoviedb.org/3/movie/{tmdb}/videos?api_key={api_key}&language=en-US"

    response_trailer = requests.get(trailer_find)
    response_trailer = response_trailer.json()
   
    for i in range(len(response_trailer["results"])):
        if (response_trailer["results"][0]['site'] == "YouTube"):
            if(response_trailer["results"][0]['type'] == "Trailer"):
                full_link = response_trailer["results"][i]["key"]
                print("Get full_link:",full_link)  
                full_link = crud.update_movie(tmdb).watch_link
                print("Commit this link to db:",full_link)
model.db.session.commit()



















# #Seed social media page

# person_list = ["2782707","1652045"]
# #kelly "1663195"
# #Social Media Link
# for person in person_list:
#     social_media_find= f"https://api.themoviedb.org/3/person/{person}/external_ids?api_key={api_key}&language=en-US"
    
#     response = requests.get(social_media_find)
#     response = response.json()
    
        
#     #Add social media to db
#    crud.updateInstagramlink
   
#    (actor_name=response["name"],dob=response["birthday"],gender=response["gender"],other_name=response["also_known_as"],biography=response["biography"],headshot=response["profile_path"])



