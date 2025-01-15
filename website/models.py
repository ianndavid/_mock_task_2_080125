#Where databases will be held and managed
from flask import Flask
import flask_sqlalchemy
from db_file import db
from flask_login import UserMixin
from datetime import date, time, datetime







#Database for the user
class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    
    bookings = db.relationship('Booking', lazy=True)

    def remove(self):
        db.session.delete(self)

    def __repr__(self):
        return f'<User {self.username}>'
    
    #Booking database
class Booking(db.Model):
        booking_id = db.Column(db.Integer, primary_key=True)
        amount_people = db.Column(db.Integer)
        date = db.Column(db.String(120))
        #Reference to user who made booking
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
        
        user = db.relationship('User', back_populates='bookings')

        def __repr__(self):
            return f'<Booking {self.user.username}, {self.amount_people}, {self.date}>'