from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import LoginManager, UserMixin
#password hashing
from werkzeug.security import generate_password_hash, check_password_hash
#generating random id
import uuid

#login manager
login = LoginManager()

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key=True)
    first_name = db.Column(db.String(100), nullable=True, default='')
    last_name = db.Column(db.String(100), nullable=True, default='')
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String, nullable=True, default='')
    data_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, username, email, password, first_name='', last_name=''):
        self.id = str(uuid.uuid4())
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = generate_password_hash(password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'firstname': self.first_name,
            'lastname': self.last_name,
            'datecreated': self.data_created
        }

class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(100), nullable=False)
    startdate = db.Column(db.Date(), nullable=True, default='')
    enddate = db.Column(db.Date(), nullable=True, default='')
    description = db.Column(db.String(200), nullable=True, default='')
    price = db.Column(db.String(20), nullable=True, default='')

    def to_dict(self):
        return {
            'id': self.id,
            'subject': self.subject,
            'startdate': self.startdate,
            'enddate': self.enddate,
            'description': self.description,
            'price': self.price
        }
