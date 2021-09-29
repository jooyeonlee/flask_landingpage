from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.forms import UserSignupForm
from app.models import db, User

users = Blueprint('user', __name__, template_folder='user_templates')

@users.route('/signup', methods=['GET', 'POST'])
def signup():
    form = UserSignupForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            print('form validated')
            # create user instance
            print(form.email.data)
            newuser = User(email=form.email.data, first_name=form.first_name.data, last_name=form.last_name.data, password=form.password.data)

            db.session.add(newuser)
            db.session.commit()

            flash(f'New User {newuser.email} has been successfully created', category='alert-info')
        else:
            flash('You entered incomplete data, please try again', category='alert-warning')
        #return redirect(url_for('home'))
    # elif request.method == 'GET'
    return render_template('signup.html', form=form)
