from project.models.users_model import User
from project.models.attendance_model import Attendance
from project.db import attendance_collection
from datetime import datetime

def add_attendance(user: User, teacher: User, topic: str | None=None) -> None:
    name = user['name']
    section = user['section']
    number = user['number']

    attendance = Attendance(
        student=User(name=name, section=section, number=number),
        teacher=teacher,
        date=datetime.now(),
        topic=topic
    )

    attendance_collection.insert_one(attendance.dict())