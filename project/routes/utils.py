from flask import Blueprint, render_template

app = Blueprint('utils', __name__)

@app.route('/')
def index():
    return render_template('index.html')