from flask import Blueprint, jsonify
from app.models import Lesson, db

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/lessons', methods=['GET'])
def lessons():
    '''
    [GET] /api/lessons
    Provides a list of all lessons in our database
    '''
    #query our database to get all of our current lesson data
    lessons = {a.subject: a.to_dict() for a in Lesson.query.all()}
    return jsonify(lessons)