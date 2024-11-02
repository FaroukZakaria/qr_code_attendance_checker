import datetime, bcrypt
from flask_jwt_extended import create_access_token, create_refresh_token
from project.db import *
from flask import request, jsonify, Blueprint, render_template
from project.models.users_model import User
from project.controllers.user_controller import *

user_routes = Blueprint('user_routes', __name__)


@user_routes.route('/signup', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('signup.html')
    
    data = request.get_json()
    name = data.get('name')
    section = int(data.get('section'))
    number = int(data.get('number'))
    password = data.get('password')

    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    if (get_user_by_section_and_number(section, number)):
        return jsonify({'message': 'User already exists'}), 400
    
    create_user(User(
        name=name,
        section=section,
        number=number,
        password=hashed_password,
        role='student'
        ))

    return jsonify({'message': 'User registered successfully'}), 201

@user_routes.route('/signin', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('signin.html')

    data = request.get_json()
    section = int(data.get('section'))
    number = int(data.get('number'))
    password = data.get('password')

    user = get_user_by_section_and_number(section, number)
    if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
        access_token = create_access_token(str(user['_id']), expires_delta=datetime.timedelta(minutes=15))
        refresh_token = create_refresh_token(str(user['_id']), expires_delta=datetime.timedelta(days=7))
        return jsonify({'access_token': access_token, 'refresh_token': refresh_token, 'role': user['role']}), 200

    return jsonify({'message': 'Invalid credentials'}), 401