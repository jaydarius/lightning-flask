import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

from jay_site.config import Config

app = Flask(__name__)  # we create our Flask instance once on the package init
app.config.from_object(Config)
db = SQLAlchemy(app)  # we create our SQL Map instance once on the package init
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

mail = Mail(app)

from jay_site.users.routes import users
from jay_site.posts.routes import posts
from jay_site.main.routes import main

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)