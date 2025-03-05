from flask import Blueprint
from flask import Flask, render_template, session, redirect, request, flash, url_for
from models import User
from db_file import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user,login_required,logout_user,current_user

#where logins will be handled and authentication


auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET','POST'])
def Login():
    if request.method == 'POST':
        #Getting user input from the forms
        username = request.form.get('username')
        password = request.form.get('password')
        #Checking is database already has a user/email that the user inputed
        user = User.query.filter_by(username=username).first()
        if user:
            #Checking if password inputed is correct for username inputed
            if check_password_hash(user.password, password):
                #flashes a green success message and redirects user to home page
                flash('You logged in successfully', category='success')
                login_user(user, remember=True)
                return redirect(url_for('frt.home',username=username))
            else:
                #Flashes a red error message
                flash('incorrect password', category='error')
        else:
            flash('Username does not exist',category='error')
    return render_template('login.html',user=current_user)


@auth.route('/signup', methods=['GET','POST'])
def Signup():
    #Post requesting is getting information
    if request.method == 'POST':
        #Getting user input from the forms
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        
        #Checking is database already has a user/email that the user inputed
        
        check_username = User.query.filter_by(username=username).first()
        check_email = User.query.filter_by(email=email).first()
        
        #If Email or username is in use will return an error
        if check_email:
            flash('Email is in use', category='error')
        elif check_username:
            flash('Username is taken', category='error')
        #Input validation testing
        elif len(email) < 4:
            flash('Email must be more than 4 characters', category='error')
        elif password != password2:
            flash('Passwords do not match', category='error')
        elif len(password) < 7:
            flash('Password must be more than 7 characters', category='error')
        else:
            #Creating the user if conditions are met
            new_user = User(email=email,username=username,password=generate_password_hash(password, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user,remember=True)#Kepp user in login session
            flash('Account successfully made', category='success')
            return redirect(url_for('frt.home',username=username))

    return render_template('signup.html', user=current_user)


@auth.route('/logout')
@login_required #User must be logged in to access this page
def Logout():
    logout_user()
    return redirect(url_for('auth.Login'))


@auth.route('/profile', methods=['GET', 'POST'])
@login_required  # User must be logged in to access this page
def profile():
    #Allowing user to change their data
    
    
    if request.method == 'POST':
        # Getting user input from the form
        email = request.form.get('email')
        username = request.form.get('username')

        # Checking if the email is already taken 
        check_email = User.query.filter_by(email=email).first()
        check_username = User.query.filter_by(username=username).first()

        if check_email:
            flash('Email is in use', category='error')
        if check_username:
            flash('Username is in use', category='error')
        else:
            # Update user data if all validations pass
            current_user.username = username
            current_user.email = email
            db.session.commit()  # Commit the changes to the database
            flash('Profile updated successfully!', category='success')
            return redirect(url_for('auth.profile'))  # Redirect to the same profile page after update

    return render_template('profile.html', user=current_user)


@auth.route('/remove', methods=['GET', 'POST'])
@login_required
def remove():
    current_user.remove()
    db.session.commit()
    return redirect(url_for('auth.Login'))



#remember to do the same thing for the user and allow suer to make changes