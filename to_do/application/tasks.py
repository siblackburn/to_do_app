from flask import Blueprint, jsonify, request, render_template

from . import db
from .models import To_do

TasksApi = Blueprint('tasks_api', __name__)

# this lives under /books/create, because this file has been declared as /books (see routes.py)
#deb session is contained in config - needs to point to mysql

#/books/create is the url because the create method is contained in books API
@TasksApi.route('/welcome')
def tasks_user():
    return render_template('Tasks_welcome.html')


@TasksApi.route('/create', methods=['POST']) # can create more than one method here (e.g. POST, GET etc)
def create_task():

    try:
        task = To_do.from_dict(request.json)
    except KeyError as e:
        return jsonify(f'Missing key: {e.args[0]}'), 400

    db.session.add(task)
    db.session.commit()
    return jsonify(), 200

#different methods can have the same path because they're calling different methods. The method AND the path make them unique
@TasksApi.route('/<id>', methods=['GET'])  #this means we're going to get something by requesting it after the /
def get_task(id):
    task = To_do.query.filter(To_do.id == id).first_or_404()
    return jsonify(task.to_dict()), 200


@TasksApi.route('/<id>', methods=['DELETE']) # can create more than one method here (e.g. POST, GET etc)
def delete_task(id):
    try:
        task = To_do.query.filter(To_do.id == id).first_or_404()
    except KeyError as e:
        return jsonify(f'Missing key: {e.args[0]}'), 400

    db.session.delete(task)
    db.session.commit()
    return 'delete successful', 200


@TasksApi.route('/modify/<id>', methods=['PUT']) #http://localhost:5000/tasks/modify/1
def modify(id):
    try:
        modified_item = To_do.from_dict(request.json)

    except KeyError as e:
        return jsonify(f'Missing key: {e.args[0]}'), 400

    old_task = To_do.query.filter(To_do.id == id).first()
    old_task.due_date = modified_item.due_date
    old_task.description = modified_item.description

    db.session.commit()
    return jsonify(), 200
