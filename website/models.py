#Where databases will be held and managed
from flask import Flask
import flask_sqlalchemy
from db_file import db
from flask_login import UserMixin





class Booking(db.Model):
    booking_id = db.Column(db.Integer, primary_key=True)
    amount_people = db.Column(db.Integer)
    date = db.DateTime(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

#Database for the user
class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    bookings = db.relationship('Booking')

    def remove(self):
        db.session.delete(self)

