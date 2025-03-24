from models.user import User
from typing import List

class UsersRepository:
    users: List[User] = []

    @classmethod
    def add_user(cls, user: User):
        cls.users.append(user)

    @classmethod
    def get_user_by_email(cls, email: str) -> User | None:
        return next((user for user in cls.users if user.email == email), None)