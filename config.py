from flask import Flask
from data import db_session
from data.types import Object, ObjectGroup, Field, Relation

app = Flask(__name__)
app.config['SECRET_KEY'] = 'h6t8ohg5^RVG767uvtfgv7y567V GFtcftrydud'
