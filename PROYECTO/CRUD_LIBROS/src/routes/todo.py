from flask import Blueprint

from services.todo import create_todo_service, get_todos_service, get_todo_service, update_todo_service, delete_todo_service

todo = Blueprint('todo', __name__)

@todo.route('/', methods=['GET'])
def get_todos():
    return get_todos_service()

@todo.route('/<id>', methods=['GET'])
def get_todo(id):
    return get_todo_service(id)

@todo.route('/', methods=['POST'])
def create_todo():
    return create_todo_service()

@todo.route('/<id>', methods=['PUT'])
def update_todo(id):
    return update_todo_service(id)

@todo.route('/<id>', methods=['DELETE'])
def delete_todo(id):
    return delete_todo_service(id)
