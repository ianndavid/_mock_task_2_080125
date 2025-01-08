from flask import Blueprint, render_template
from flask import Flask

#where main pages will be handled
frt = Blueprint('frt', __name__)

#Main routes
@frt.route('/')
def home():
    return render_template('home.html')

@frt.route('/shop')
def Shop():
    return render_template('shop.html')


@frt.route('/faq')
def FAQ():
    return '<h1> faw <h1>'


@frt.route('/cart')
def Cart():
    return '<h1> cart <h1>'

@frt.route('/booking')
def Booking():
    return '<h1> bok <h1>'