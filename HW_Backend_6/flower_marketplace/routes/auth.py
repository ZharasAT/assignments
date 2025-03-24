import jwt
import datetime
from fastapi import APIRouter, Form, Request, HTTPException, Response, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from models.user import User
from repo.users import UsersRepository
from dependencies import verify_jwt
import os

SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/signup")
def signup_form(request: Request):
    return templates.TemplateResponse("auth/signup.html", {"request": request})

@router.post("/signup")
def signup(
        email: str = Form(...),
        first_name: str = Form(...),
        last_name: str = Form(...),
        password: str = Form(...)
):
    """User Registration"""

    if UsersRepository.get_user_by_email(email):
        raise HTTPException(status_code=400, detail="The user already exists")

    new_user = User(
        id=len(UsersRepository.users) + 1,
        email=email,
        first_name=first_name,
        last_name=last_name,
        password=password
    )

    UsersRepository.add_user(new_user)
    return {"message": "Registration successful! Go to /login"}

@router.get("/login", include_in_schema=True, response_class=HTMLResponse)
def login_form(request: Request):
    print("✅ GET /login вызван")
    return templates.TemplateResponse("auth/login.html", {"request": request})

@router.post("/login")
def login(
        response: Response,
        email: str = Form(...),
        password: str = Form(...)
):
    """User login"""

    user = UsersRepository.get_user_by_email(email)
    if not user or user.password != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # JWT-token creation
    payload = {
        "sub": user.email,
        "exp": datetime.datetime.now(datetime.UTC) + datetime.timedelta(hours=2)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    # sending the token to cookie
    response.set_cookie(key="token", value=token, httponly=True)

    return {"message": "login successful"}

@router.get("/profile", response_class=HTMLResponse)
def profile_page(request: Request, user_data: dict = Depends(verify_jwt)):
    """Returns user data if token exists"""
    email = user_data.get("sub")
    user = UsersRepository.get_user_by_email(email)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user_data_safe = {
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name
    }

    return templates.TemplateResponse("auth/profile.html", {
        "request": request,
        "user": user_data_safe
    })

print("✅  Все маршруты загружены:")
print(router.routes)