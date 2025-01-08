from flask import Blueprint
from flask import Flask, render_template, session, redirect, request, flash
#where logins will be handled and authentication


auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET','POST'])
def Login():
    data= request.form['']
    return render_template('login.html')


@auth.route('/signup', methods=['GET','POST'])
def Signup():
    #Post requesting is getting information
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be more than 4 characters', category='error')
        elif password != password2:
            flash('Passwords do not match', category='error')
        elif password < 7:
            flash('Password must be more than 7 characters', category='error')
        else:
            flash('account successfully made')


    return render_template('signup.html')


@auth.route('/logout')
def Logout():
    return


@auth.route('/profile')
def Profile():
    return

