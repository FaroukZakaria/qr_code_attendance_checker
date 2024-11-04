from pydantic import BaseModel
from project.models.users_model import User
from datetime import datetime

class Attendance(BaseModel):
    student: User
    teacher: User
    date: datetime
    topic: str | None