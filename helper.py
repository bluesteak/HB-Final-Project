
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

import requests
import json
import crud
api_key = "ca04f28350cde67bc24470dfe961b3dd"
#The list of TMDB id for actor
person_id = ["1663195","2782707"]
#Actor Data
for num in range(len(person_id)):
    actor_find = f"https://api.themoviedb.org/3/person/{person_id[num]}?api_key={api_key}&language=en-US"
    #movie_find = f"https://api.themoviedb.org/3/person/{person_id}/movie_credits?api_key={api_key}&language=en-US"
    response = requests.get(actor_find)
    response = response.json()
# #Create json file to view
# response = response.json()
# with open("dummydataactor.json","w") as f:
#     json.dump(response, f, indent=4)