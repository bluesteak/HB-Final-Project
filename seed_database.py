"""Script to seed database."""

import os
import json
from datetime import datetime

import model
import server
import seed_database

os.system("dropdb actors")
os.system("createdb actors")

model.connect_to_db(server.app)
model.db.create_all()


# db_actors = crud.create_actors(name)
# actors_in_db.append(db_actors)

# model.db.session.add_all(actors_in_db)
# model.db.session.commit()