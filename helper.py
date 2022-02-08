import requests
import json

api_key = "ca04f28350cde67bc24470dfe961b3dd"
person_id = "1663195"
# #Search actor from API
# actor_url = f"https://api.themoviedb.org/3/search/person?api_key={api_key}&query=Kelly+Marie+Tran"
# #Get a list of person -> get their imdb id from actor_url -> use that person_id and request for their infor
# #need to store their imdb id 

# response = requests.get(actor_url)
# response = response.json()

# #Create json file
# with open("personid.json","w") as f:
#     json.dump(response, f, indent=4)


movie_find = f"https://api.themoviedb.org/3/person/{person_id}/movie_credits?api_key={api_key}&language=en-US"

moviedata = requests.get(movie_find)
moviedata = moviedata.json()

for i in range(len(moviedata["cast"])):
    print(moviedata["cast"][i]["original_title"])
    print(moviedata["cast"][i]["character"])

#Create json file to view
with open("movielist.json","w") as f:
    json.dump(moviedata, f, indent=4)