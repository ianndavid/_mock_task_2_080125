#To stop circular imports, db will be called from this file
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()