from app.forms import newLectureForm
from flask import Blueprint, render_template, request, url_for, flash
from app.models import db, Lesson

lectures = Blueprint('lecture', __name__, template_folder='lecture_templates')

@lectures.route('/lecture', methods=["GET"])
def lecturelist():
    return render_template('lecture.html', lecture_new=None)

@lectures.route('/addlecture', methods=["GET", "POST"])
def addlecture():
    form = newLectureForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            newlecture = Lesson(subject=form.subject.data, startdate=form.start_date.data.strftime('%Y-%m-%d'), enddate=form.end_date.data.strftime('%Y-%m-%d'), description=form.description.data, price=form.price.data)
            db.session.add(newlecture)
            db.session.commit()
        else:
            print('fail')
        return render_template('lecture.html', lecture_new=newlecture.to_dict())
    return render_template('addlecture.html', form=form)