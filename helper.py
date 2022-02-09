
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

import requests
import json
import crud
api_key = "ca04f28350cde67bc24470dfe961b3dd"
#The list of TMDB id for actor
personid_list = ["1663195","2782707"]
#Actor Data
for person in personid_list:
    actor_find = f"https://api.themoviedb.org/3/person/{person}?api_key={api_key}&language=en-US"
    response = requests.get(actor_find)
    response = response.json()
    with open("dummydataactor.json","a") as f:
        json.dump(response, f, indent=4)
    for i in response:
        print(i)
#Create json file to view
# response = response.json()
