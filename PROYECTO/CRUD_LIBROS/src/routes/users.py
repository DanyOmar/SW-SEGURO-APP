from flask import Blueprint

from services.users import create_user_service, get_users_service, get_user_service, update_user_service, delete_user_service

user = Blueprint('user', __name__)

@user.route('/', methods=['GET'])
def get_users():
    return get_users_service()

@user.route('/<id>', methods=['GET'])
def get_user(id):
    return get_user_service(id)

@user.route('/', methods=['POST'])
def create_user():
    return create_user_service()

@user.route('/<id>', methods=['PUT'])
def update_user(id):
    return update_user_service(id)

@user.route('/<id>', methods=['DELETE'])
def delete_user(id):
    return delete_user_service(id)
