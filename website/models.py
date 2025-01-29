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
    
    hotel_bookings = db.relationship('Hotel_Booking', lazy=True)

    def remove(self):
        db.session.delete(self)

    def __repr__(self):
        return f'<User {self.username}>'
    
    #Booking database
class Booking(db.Model):
        booking_id = db.Column(db.Integer, primary_key=True)
        amount_adults = db.Column(db.Integer)
        amount_children = db.Column(db.Integer)
        date = db.Column(db.String(120))
        #Reference to user who made booking
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
        
        user = db.relationship('User', back_populates='bookings')

        def __repr__(self):
            return f'<Booking {self.user.username}, {self.amount_people}, {self.date}>'
            
        def is_active(self):
            return True
        #Allows Database to be deleted
        def remove(self):
            db.session.delete(self)

    #Booking Hotel Tickets
class Hotel_Booking(db.Model):
    
        Hotel_id = db.Column(db.Integer, primary_key=True)
        Hotel_Check_in = db.Column(db.String(120))
        Hotel_Check_Out = db.Column(db.String(120))
        Hotel_Beds = db.Column(db.Integer)
        
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
        
        user = db.relationship('User', back_populates='hotel_bookings')
    
        def remove(self):
            db.session.delete(self)