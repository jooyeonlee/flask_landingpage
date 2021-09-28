from flask import Flask
from config import Config
 
from .lecture.routes import lectures
from .meetup.routes import meetups

app = Flask(__name__)

app.register_blueprint(lectures)
app.register_blueprint(meetups)

app.config.from_object(Config)

from . import routes

