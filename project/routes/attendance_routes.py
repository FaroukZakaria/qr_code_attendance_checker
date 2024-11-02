from flask import Blueprint, request, jsonify, render_template
from project.controllers.token_controller import verify_token
from project.controllers.attendance_controller import add_attendance

app = Blueprint('attendance', __name__)

@app.route('/record-attendance', methods=['GET', 'POST'])
def record_attendance():
    if request.method == 'GET':
        return render_template('record_attendance.html')
    token = request.cookies.get('access_token')
    if not token or not verify_token(token):
        token = request.cookies.get('refresh_access_token')
        if not token or not verify_token(token):
            return render_template('login.html', message="You need to login to access this page")
    
    data = request.get_json()
    name = data.get('name')
    section = data.get('section')
    number = data.get('number')

    add_attendance(name, section, number)
    return jsonify({'message': 'Attendance recorded'}), 200