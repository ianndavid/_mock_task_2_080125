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


#Cart page
@frt.route('/cart')
def Cart():
    amountadults = session.get('amountadults', None)
    amountchildren = session.get('amountadults', None)
    totalamount = session.get('totalamount')
    
    return render_template('cart.html', amountadults=amountadults,user=current_user,amountchildren=amountchildren,totalamount=totalamount)




#try get Booking
@frt.route('/booking', methods=['GET','POST'])
@login_required
def Book():
        if request.method == 'POST':
            #recieving users infomation
            amount_adults = request.form.get('booking_amount_adults')
            amount_children = request.form.get('booking_amount_children')
            date = request.form.get('booking_date')
            name = request.form.get('booking_name')

            #Adds booking to database
            new_booking = Booking(amount_adults=amount_adults, date=date,amount_children=amount_children)
            db.session.add(new_booking)
            db.session.commit()
            flash('Booking successful', category='success')
            
            amount_adults = new_booking.amount_adults
            amount_children = new_booking.amount_children
            booking_date = new_booking.date
            
            #Adult and children ticket prices
            Adult_cost = amount_adults * 12.45
            children_cost = amount_children * 6.75
            total = Adult_cost + children_cost
            total = round(total, 3)
            
            #Session for them to be called in other pages such as cart
            session['amountadults'] = amount_adults
            session['amountchildren'] = amount_children
            session['totalamount'] = total
            
            #passing data into booking.html
            return render_template('booking.html',booking_id=current_user.id, user=current_user,booking_date=booking_date ,name=name, amount_children=amount_children,amount_adults=amount_adults,total=total)
        return render_template('booking.html', user=current_user)
    

#For deleting booking
@frt.route('/deletebooking', methods=['GET', 'POST'])
@login_required
def deletebooking():
        session.clear()
        return redirect(url_for('frt.Book'))

#Complete delete booking and hotel booking