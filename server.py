""" Server for Cannes Pineapple movie database app. """

from flask import Flask

from flask import (Flask, render_template, request, flash, session,
                   redirect)

from jinja2 import StrictUndefined 
import requests
app = Flask(__name__)
app.secret_key = "BakedPineapple"
app.jinja_env.undefined = StrictUndefined

#HomePage
@app.route("/")
def homepage():
    """ Show homepage """
    return render_template("homepage.html")

@app.route("/movies")
def movies():
    
    response = requests.get("")
    data = response.json()

@app.route("/actors")
def actors():
 
    return render_template("actors.html")
    # response = requests.get("https://api.themoviedb.org/3/search/person?api_key=ca04f28350cde67bc24470dfe961b3dd&language=en-US&query=nguyen&page=1&include_adult=false")
    # data = response.json()
    # return data

@app.route("/actor_detail")
def actor_detail(actor_id):
 

 def show_movie(actor_id):
    """Show details on a particular movie."""

    actor = crud.get_actor_by_id(actor_id)
    return render_template("actor_detail.html",actor=actor)




if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True)
