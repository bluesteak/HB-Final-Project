<img src="/static/img/logo_1.png" alt="Cannes Pineapple logo" width="300px"/>
<h2>Cannes Pineapple</h2>
Cannes Pineapple (CP) is a responsive web application created with the purpose of viewing information about Asian American actors and their movies. CP showcases Asian American actors and celebrates Asian representation in film. CP maintains a database of movie and actor information, including movie title, release year, character, actor, etc. User are able to create an account and create a movie or add to their favorite list. The movie data is obtained from TMDB API which is fetched and stored into SQL database. 



<h2>Tech Stack</h2>

* **Backend:** Python, SQLAlchemy, Jinja, Flask
* **Frontend:** HTML, CSS, Bootstrap, JavaScript
* **Database:** PostgreSQL
* **API's:** TMDB API

<h2>Installation</h2>
<h4>Requirements</h4>
Install Python3 and Postgre
<h4>Setup virtual environment</h4>
Set up and activate a virtual environment with virtualenv:
```
cd Project
pip3 install virtualenv
virtualenv env
source env/bin/activate
pip3 install -r requirements.txt
```
Clone the repository:

```
https://github.com/bluesteak/HB-Final-Project.git
```
<h4>Setup the database</h4>

```
python3 seed_database.py
```

```
python3 seed_additional.py
```

<h4>Running the application:</h4>

```
python3 server.py
Navigate to localhost:5000
```
<h2>About Developer</h2>
Quyen Truong <br>
qtruongk@gmail.com <br>
<br> Quyen received the Phenomenal Woman Scholarship to attend Hackbright Academy's Software Engineering Fellowship Program in 2021. She is an aspiring developer interested in the intersection of code and art. Quyen balances her busy schedule as a full-time employee and part-time student by having a creative outlet. She loves creating to express herself, making miniature models and 3D characters in Blender software.
