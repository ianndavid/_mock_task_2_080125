from flask import Blueprint
from flask import Flask, render_template, session, redirect, request, flash, url_for
from flask_login import login_user,login_required,logout_user,current_user
from db_file import db
from models import Booking
from models import User
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


#try get Booking
@frt.route('/booking', methods=['GET','POST'])
@login_required
def Book():
        if request.method == 'POST':
            amount_people = request.form.get('booking_amount')
            date = request.form.get('booking_date')

            new_booking = Booking(amount_people=amount_people, date=date)
            db.session.add(new_booking)
            db.session.commit()

            flash('Booking successful', category='success')
            return redirect(url_for('frt.bookingauth', booking_id = new_booking.booking_id))

        return render_template('booking.html', user=current_user)
    
@frt.route('/bookingauth', methods=['GET','POST'])
@login_required
def bookingauth():
    
    return render_template('bookingauth.html', user=current_user, booking_id=booking_id)
    