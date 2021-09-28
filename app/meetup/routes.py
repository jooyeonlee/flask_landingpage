from flask import Blueprint, render_template

meetups = Blueprint('meetup', __name__, template_folder='meetup_templates')

@meetups.route('/meetup')
def meetuplist():
    return render_template('meetup.html')