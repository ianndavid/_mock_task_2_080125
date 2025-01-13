from flask import Blueprint, render_template
from flask import Flask
from flask_login import login_user,login_required,logout_user,current_user
#where main pages will be handled
frt = Blueprint('frt', __name__)

#Main routes
@frt.route('/')
def home():
    return render_template('home.html', user=current_user)

@frt.route('/faq')
def FAQ():
    return render_template('faq.html')


@frt.route('/cart')
def Cart():
    return render_template('cart.html')

@frt.route('/booking')
def Booking():
    return render_template('booking.html')