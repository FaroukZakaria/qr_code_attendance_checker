from project.db import users_collection
from project.models.users_model import User, AdminUser
from project.routes.utils import verify_token

def create_user(user: User):
    users_collection.insert_one(user.dict())

def create_admin(admin: AdminUser):
    users_collection.insert_one(admin.dict())

def get_user_by_section_and_number(section: int, number:int):
    return users_collection.find_one({'section': section, 'number': number})

def get_admin(email: str):
    return users_collection.find_one({'email': email})

def get_user_by_token(token: str):
    users_collection.find_one({'_id': verify_token(token)['sub']})