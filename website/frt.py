from flask import Blueprint
from flask import Flask, render_template, session, redirect, request, flash, url_for
from flask_login import login_user,login_required,logout_user,current_user
from db_file import db
from models import Booking
from models import Hotel_Booking
from models import User
from datetime import datetime

#where main pages will be handled
frt = Blueprint('frt', __name__)



#Main routes
@frt.route('/')
def home():
    return render_template('home.html', user=current_user)

@frt.route('/faq')
def FAQ():
    return render_template('faq.html',user=current_user)


#Cart page
@frt.route('/cart', methods=['GET','POST'])
@login_required
def Cart():
    if request.method == 'GET':
        
        amountadults = session.get('amountadults', None)
        amountchildren = session.get('amountadults', None)
        total = session.get('total',)


        hotel_total = session.get('hotel_total', None)
        Hotel_Check_in = session.get('Hotel_Check_in', None)
        Hotel_Check_Out = session.get('Hotel_Check_Out', None)
        Hotel_Beds = session.get('Hotel_Beds', None)


        total = int(float(total))
        hotel_total = int(float(hotel_total))
        
        
        overall = hotel_total + total
        
        return render_template('cart.html', 
                           amountadults=amountadults,
                           user=current_user,
                           amountchildren=amountchildren,
                           total=total,
                           Hotel_Check_Out = Hotel_Check_Out,
                           Hotel_Beds=Hotel_Beds,
                           Hotel_Check_in=Hotel_Check_in,
                           hotel_total=hotel_total,
                           overall=overall )
    return render_template('cart.html', 
                           amountadults=amountadults,
                           user=current_user,
                           amountchildren=amountchildren,
                           total=total,
                           Hotel_Check_Out = Hotel_Check_Out,
                           Hotel_Beds=Hotel_Beds,
                           Hotel_Check_in=Hotel_Check_in,
                           hotel_total=hotel_total,
                           overall=overall
                           )


#try get Booking
@frt.route('/booking', methods=['GET','POST'])
@login_required
def Book():
        if request.method == 'POST':
            total = 0
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
            
            #Adult and children ticket prices calculations
            Adult_cost = amount_adults * 12.45
            children_cost = amount_children * 6.75
            
            total = Adult_cost + children_cost
            total = round(total, 3)
            
            #Session for them to be called in other pages such as cart
            session['amountadults'] = amount_adults
            session['amountchildren'] = amount_children
            session['total'] = total
            
            #passing data into booking.html
            return render_template('booking.html',booking_id=current_user.id, user=current_user,booking_date=booking_date ,name=name, amount_children=amount_children,amount_adults=amount_adults,total=total)
        return render_template('booking.html', user=current_user)
    

@frt.route('/hotelbooking', methods=['GET', 'POST'])
@login_required
def HotelBook():
        
        if request.method == 'POST':
        
            Hotel_Check_in = request.form.get('Hotel_Check_in')
            Hotel_Check_Out = request.form.get('Hotel_Check_Out')
            Hotel_Beds = request.form.get('Hotel_Beds')
            
            new_hotel_booking = Hotel_Booking(Hotel_Check_in=Hotel_Check_in,Hotel_Check_Out=Hotel_Check_Out,Hotel_Beds=Hotel_Beds)
            db.session.add(new_hotel_booking)
            db.session.commit()
            flash('Hotel Booking successful', category='success')
            
            Hotel_Check_in = new_hotel_booking.Hotel_Check_in
            Hotel_Check_Out = new_hotel_booking.Hotel_Check_Out
            Hotel_Beds = new_hotel_booking.Hotel_Beds
            
            # Convert the strings to datetime objects
            date1 = datetime.strptime(Hotel_Check_in, "%Y-%m-%d")
            date2 = datetime.strptime(Hotel_Check_Out, "%Y-%m-%d")

                # Calculating the time difference
            difference_in_time = date2 - date1
                # Calculating the number of days between the two dates
            difference_in_days = difference_in_time.days
            hotel_total = difference_in_days * 15.45
            hotel_total = round(hotel_total, 3) 

            #Sessioning them so they can be called and showed in different pages 
            session['Hotel_Check_in'] = Hotel_Check_in
            session['Hotel_Check_Out'] = Hotel_Check_Out
            session['Hotel_Beds'] = Hotel_Beds
            session['hotel_total'] = hotel_total
            session['difference_in_days'] = difference_in_days
            
            return render_template('hotelbooking.html', Hotel_Check_in=Hotel_Check_in,Hotel_Check_Out=Hotel_Check_Out,Hotel_Beds=Hotel_Beds,difference_in_days=difference_in_days,user=current_user,hotel_total=hotel_total) 
        return render_template('hotelbooking.html',user=current_user)


@frt.route('/choice')
def Choice():
    return render_template('choice.html',user=current_user)


#For deleting booking
@frt.route('/deletebooking', methods=['GET', 'POST'])
@login_required
def deletebooking():
        session.clear()
        return redirect(url_for('frt.Cart'))

#Complete delete booking and hotel booking

