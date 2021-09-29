from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
#password hashing
from werkzeug.security import generate_password_hash
#generating random id
import uuid

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.String, primary_key=True)
    first_name = db.Column(db.String(100), nullable=True, default='')
    last_name = db.Column(db.String(100), nullable=True, default='')
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String, nullable=True, default='')
    data_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, email, id='', first_name='', last_name='', password=''):
        self.id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = generate_password_hash(password)

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
