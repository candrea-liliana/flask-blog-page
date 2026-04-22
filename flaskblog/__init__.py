from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app) # Set a DB instance
bcrypt = Bcrypt(app) # Set an encrypting instance
login_manager = LoginManager(app) # Set a Login manager instance
login_manager.login_view = 'users.login' # Set the login manager by the login view
login_manager.login_message_category = 'info'

mail = Mail(app)

from flaskblog.main.routes import main
from flaskblog.users.routes import users
from flaskblog.posts.routes import posts

app.register_blueprint(main)
app.register_blueprint(users)
app.register_blueprint(posts)
