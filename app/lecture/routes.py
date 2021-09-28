from flask import Blueprint, render_template

lectures = Blueprint('lecture', __name__, template_folder='lecture_templates')

@lectures.route('/lecture', methods=["GET"])
def lecturelist():
    return render_template('lecture.html')