from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
import os 
from flask_login import LoginManager 
from models import User
from db_file import db


#Creating a database

db_name = 'database1.db'





#This is for running the app
def start_app():
    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'H432HDF832HBDNGGFYG'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database1'
    db.init_app(app)
    #Login manager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.Login'
    login_manager.init_app(app)
    
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    #Importing the python files that hold the webpages
    from frt import frt
    from auth import auth
    app.register_blueprint(frt, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    from models import User
    
    create_database(app)
    
    
    return app

#Creating the database
def create_database(app):
    data_path = os.path.join('website', db_name)
    if not os.path.exists(data_path):#Checking if it exists
        with app.app_context():
            db.create_all()#Creating it