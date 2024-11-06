from flask import Blueprint, request, jsonify
from project.controllers.token_controller import verify_token
from project.db import users_collection
from bson.objectid import ObjectId

app = Blueprint('token', __name__)

@app.route('/check-auth')
def check_auth():
    token = request.cookies.get('access_token')
    if not token or not verify_token(token):
        return jsonify({'message': 'Token is invalid or expired'}), 401
    is_admin = request.cookies.get('role') == 'admin'
    user_name = users_collection.find_one({'_id': ObjectId(verify_token(token)['sub'])})['name']
    return jsonify({'name': user_name,'admin': is_admin}), 200