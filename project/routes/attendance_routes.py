from flask import Blueprint, request, jsonify, render_template
from project.controllers.token_controller import verify_token
from project.controllers.attendance_controller import add_attendance
from project.db import users_collection

app = Blueprint('attendance', __name__)

@app.route('/record-attendance', methods=['GET', 'POST'])
def record_attendance():
    if request.method == 'GET':
        return render_template('record_attendance.html')
    token = request.cookies.get('access_token')
    if not token or not verify_token(token):
        return jsonify({'message': 'Token is invalid or expired'}), 401



    user = users_collection.find_one({'_id': verify_token(token)['sub']})
    add_attendance(user)
    return jsonify({'message': 'Attendance recorded'}), 200