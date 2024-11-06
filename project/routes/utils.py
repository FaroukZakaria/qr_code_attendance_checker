from flask import Blueprint, render_template, request, redirect
from project.controllers.token_controller import verify_token


app = Blueprint('utils', __name__)

@app.route('/')
def index():
    token = request.cookies.get('access_token')
    if not token or not verify_token(token):
        return render_template('index.html')
    return redirect('record-attendance')