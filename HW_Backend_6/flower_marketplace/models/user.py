from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    password: str
    profile_picture: str | None = None

class User(UserCreate):
    id: int