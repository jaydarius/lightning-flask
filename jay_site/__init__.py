from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)  # we create our Flask instance once on the package init
app.config['SECRET_KEY'] = '9ada615921b3d25d6cca4208129edce0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # the 3 slashes are a relative path from the current file
db = SQLAlchemy(app)  # we create our SQL Map instance once on the package init
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from jay_site import routes