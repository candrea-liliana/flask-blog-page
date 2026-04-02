from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app) # Set a DB instance
bcrypt = Bcrypt(app) # Set an encrypting instance
login_manager = LoginManager(app) # Set a Login manager instance
login_manager.login_view = 'login' # Set the login manager by the login view
login_manager.login_message_category = 'info'

from flaskblog import routes