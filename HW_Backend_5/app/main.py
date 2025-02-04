from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from .routes import router as books_router
from .repo import BooksRepository

app = FastAPI()

templates = Jinja2Templates(directory="templates")
repository = BooksRepository()

# Home page
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

# Connecting routes from routes.py
app.include_router(books_router)