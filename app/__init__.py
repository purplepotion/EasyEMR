from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# create the flask object
app = Flask(__name__)
Bootstrap(app)
login = LoginManager(app)
# set the login view that handles flask-login
login.login_view = 'login'
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app import routes, models
