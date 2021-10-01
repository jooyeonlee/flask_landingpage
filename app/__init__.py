from flask import Flask
from config import Config
 
# blueprint
from .lecture.routes import lectures
from .meetup.routes import meetups
from .user.routes import users
from .api.routes import api

# imports for database
from .models import db, login
from flask_migrate import Migrate

app = Flask(__name__)

app.register_blueprint(lectures)
app.register_blueprint(meetups)
app.register_blueprint(users)
app.register_blueprint(api)

app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

#login manager
login.init_app(app)
login.login_view = 'home'
login.login_message = 'Please log in to see this page'
login.login_message_category = 'alert-info'

from . import routes
from . import models
