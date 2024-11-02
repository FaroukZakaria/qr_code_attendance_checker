import os
from flask_jwt_extended import JWTManager
from flask import Flask
from project.routes.user_routes import user_routes
from project.routes.utils import app as utils
from project.routes.attendance_routes import app as attendance

app = Flask(__name__)
# configure the app
app.config['JWT_SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['JWT_REFRESH_SECRET_KEY'] = os.getenv('SECRET_KEY_REFRESH')
JWTManager(app)

# define the routes
app.register_blueprint(user_routes)
app.register_blueprint(utils)
app.register_blueprint(attendance)