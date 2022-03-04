
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

import requests
import json
import crud
from bs4 import BeautifulSoup
import lxml
soup = BeautifulSoup(requests.get('https://disney.fandom.com/wiki/Raya').content,'lxml')
print(soup)

