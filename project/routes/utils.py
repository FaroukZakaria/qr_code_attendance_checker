from flask import Blueprint, render_template, request, jsonify
from project.controllers.token_controller import verify_token
from project.controllers.attendance_controller import add_attendance


app = Blueprint('utils', __name__)

@app.route('/')
def index():
    return render_template('index.html')