from flask import Flask
from config import Config
 
# blueprint
from .lecture.routes import lectures
from .meetup.routes import meetups
from .user.routes import users

# imports for database
from .models import db
from flask_migrate import Migrate

app = Flask(__name__)

app.register_blueprint(lectures)
app.register_blueprint(meetups)
app.register_blueprint(users)

app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

from . import routes
from . import models
