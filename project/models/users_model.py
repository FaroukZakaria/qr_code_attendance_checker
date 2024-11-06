from pydantic import BaseModel

# Define the User schema using Pydantic
class User(BaseModel):
    name: str
    section: int
    number: int
    password: bytes
    role: str

class AdminUser(BaseModel):
    name: str
    email: str
    password: bytes
    role: str