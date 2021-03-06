from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, SubmitField, PasswordField
from wtforms.fields.core import DateField, DecimalField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms.fields.html5 import DateField

class UserSignupForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    username = StringField('User Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit_button = SubmitField()

class UserSinginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit_button = SubmitField()

class EditUserForm(FlaskForm):
    new_firstname = StringField('First Name')
    new_lastname = StringField('Last Name')
    newpassword = PasswordField('New Password')
    confirm_password = PasswordField('Confirm Password', validators=[EqualTo('newpassword')])
    current_password = PasswordField('Current Password', validators=[DataRequired()])
    submit_button = SubmitField()

class newLectureForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired()])
    start_date = DateField('Start at', format='%Y-%m-%d')
    end_date = DateField('End at', format='%Y-%m-%d')
    description = StringField('Description')
    price = DecimalField('Price', validators=[DataRequired()])
    submit_button = SubmitField()