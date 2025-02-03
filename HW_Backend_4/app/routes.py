from fastapi import APIRouter, Request, HTTPException, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from starlette.responses import HTMLResponse

from .repo import BooksRepository

router = APIRouter()
repository = BooksRepository()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@router.get("/books", response_class=HTMLResponse)
def get_books(request: Request, page: int=1, limit: int=10):
    """Return a paginated list of books"""
    books = repository.get_all()
    start = (page - 1) * limit
    end = start + limit
    paginated_books = books[start:end]

    return templates.TemplateResponse("books/book_list.html", {
        "request": request,
        "books": paginated_books,
        "page":page,
        "has_next": end < len(books),
        "has_prev": start > 0
    })

@router.get("/books/new", response_class=HTMLResponse)
def create_book_form(request: Request):
    """Form for adding new book"""
    return templates.TemplateResponse("books/new.html", {"request": request})

@router.post("/books/new")
def create_book(
        title: str = Form(...),
        author: str = Form(...),
        year: int = Form(...),
        total_pages: int = Form(...),
        genre: str = Form(...)
):
    """Process of adding new book"""
    new_book = {
        "id": len(repository.get_all()) + 1,
        "title": title,
        "author": author,
        "year": year,
        "total_pages": total_pages,
        "genre": genre
    }
    repository.save(new_book)
    return RedirectResponse(url="/books", status_code=303)

@router.get("/books/{book_id}", response_class=HTMLResponse)
def get_book_by_id(request: Request, book_id: int):
    """Display detailed book info"""
    book = repository.get_one(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book is not found")
    return templates.TemplateResponse("books/book_detail.html", {
        "request": request,
        "book": book
    })