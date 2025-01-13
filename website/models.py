#Where databases will be held and managed
from flask import Flask
import flask_sqlalchemy
from db_file import db
from flask_login import UserMixin


#Database for the user
class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    
    def remove(self):
        db.session.delete(self)
    