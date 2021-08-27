from flask import Flask
from data import db_session
from data.types import Object, ObjectGroup, Field, Relation

TOKENS = ["default"]
app = Flask(__name__)
