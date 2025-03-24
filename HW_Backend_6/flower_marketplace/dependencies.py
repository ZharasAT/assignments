import jwt
import os
from fastapi import Cookie, HTTPException

SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")

print("✅ `auth.py`: маршруты загружаются...")

def verify_jwt(token: str = Cookie(None)) -> dict:
    """Validate JWT and return user data"""
    if not token:
        raise HTTPException(status_code=401, detail="Token missing")

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

    return payload