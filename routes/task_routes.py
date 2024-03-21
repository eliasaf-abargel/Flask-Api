
from flask import Blueprint, jsonify, request, abort
from task_models.task import Task

task_blueprint = Blueprint('tasks', __name__)
JSON_FILE = 'tasks.json'

tasks = Task.read_tasks_from_json(JSON_FILE)

@task_blueprint.route('/', methods=['GET'])
def get_all_tasks():
    return jsonify([task.to_json() for task in tasks])

@task_blueprint.route('/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task.id == task_id), None)
    return jsonify(task.to_json()) if task else abort(404)

@task_blueprint.route('/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    global tasks
    task = next((task for task in tasks if task.id == task_id), None)
    if not task:
        abort(404)
    data = request.json
    task.title = data.get('title', task.title)
    task.details = data.get('details', task.details)
    Task.write_tasks_to_json(JSON_FILE, tasks)
    return jsonify(task.to_json())


@task_blueprint.route('/', methods=['POST'])
def create_task():
    global tasks
    data = request.json
    task = Task(id=len(tasks) + 1, title=data['title'], details=data['details'])
    tasks.append(task)
    Task.write_tasks_to_json(JSON_FILE, tasks)
    return jsonify(task.to_json()), 201


@task_blueprint.route('/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    task = next((task for task in tasks if task.id == task_id), None)
    if not task:
        abort(404)
    tasks = [t for t in tasks if t.id != task_id]
    Task.write_tasks_to_json(JSON_FILE, tasks)
    return '', 204
