from project.db import users_collection

def create_user(user):
    users_collection.insert_one(user.dict())

def get_user_by_section_and_number(section: int, number:int):
    print(users_collection.find_one({'section': section, 'number': number}))
    return users_collection.find_one({'section': section, 'number': number})