from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask.scaffold import _matching_loader_thinks_module_is_package
from flask_login.utils import login_required
from werkzeug.security import check_password_hash, generate_password_hash
from app.forms import EditUserForm, UserSignupForm, UserSinginForm
from app.models import db, User
from flask_login import login_user, logout_user, current_user

users = Blueprint('user', __name__, template_folder='user_templates')

@users.route('/signup', methods=['GET', 'POST'])
def signup():
    form = UserSignupForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            print('form validated')
            # create user instance
            print(form.email.data)
            newuser = User(username=form.username.data, email=form.email.data, first_name=form.first_name.data, last_name=form.last_name.data, password=form.password.data)

            try:
                db.session.add(newuser)
                db.session.commit()
            except:
                flash(f"Username or Email already exists. Please try again", category='alert-danger')
                return redirect(url_for('user.signup'))
            flash(f'New User {newuser.email} has been successfully created', category='alert-info')
        else:
            flash('You entered incomplete data, please try again', category='alert-warning')
        return redirect(url_for('home'))
    # elif request.method == 'GET'
    return render_template('signup.html', form=form)

@users.route('/signin', methods=['GET', 'POST'])
def signin():
    form = UserSinginForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            emaildata = form.email.data
            passworddata = form.password.data

            user = User.query.filter_by(email=emaildata).first()

            if user is None or not check_password_hash(user.password, passworddata):
                flash('Incorrect username or password. Please try again', category='alert-danger')
                return redirect(url_for('user.signin'))

            login_user(user)
            flash(f'You have successfully logged in! Welcome {user.username}', category='alter-info')
            return redirect(url_for('home'))
        else:
            flash('Invalid form input. Please try again', category='alter-danger')
            return redirect(url_for('user.signin'))
    return render_template('signin.html', form=form)

@users.route('/signout', methods=['GET'])
def signout():
    logout_user()
    flash('You have successfully signed out', category='alert-info')
    return redirect(url_for('user.signin'))

@users.route('/profile', methods=['GET'])
@login_required
def profile():
    context = current_user.to_dict()
    return render_template('profile.html', **context)

@users.route('/editprofile', methods=['GET', 'POST'])
@login_required
def editprofile():
    form = EditUserForm()
    if request.method == 'POST':
        if form.validate_on_submit() and check_password_hash(current_user.password, form.current_password.data):
            if form.newpassword.data:
                current_user.password = generate_password_hash(form.newpassword.data)
            if form.new_firstname.data:
                current_user.first_name = form.new_firstname.data
            if form.new_lastname.data:
                current_user.last_name = form.new_lastname.data
            if form.newpassword.data or form.new_firstname.data or form.new_lastname.data:
                db.session.commit()
            flash('User Profile Updated!', category='alert-info')
            return redirect(url_for('user.profile'))
        else:
            flash('Invalid Form input. Please Try Again', category='alert-danger')
            return redirect(url_for('user.profile'))
    return render_template('editprofile.html', form=form)