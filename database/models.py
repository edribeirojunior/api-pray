from .db import db

class Pray(db.Document):
    name = db.StringField(required=True, unique=True)
    pray = db.StringField(required=True, unique=True)