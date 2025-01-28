from fastapi import APIRouter, Request, Query, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from repositories.cars import filter_cars_by_name, get_cars, add_car

router = APIRouter()
import os
templates = Jinja2Templates(directory=os.path.abspath("templates"))

@router.get("/cars/search", response_class=HTMLResponse)
async def search_cars(request: Request, car_name: str = Query("", alias="car_name")):
    """Car search page"""
    filtered_cars = filter_cars_by_name(car_name) if car_name else []
    return templates.TemplateResponse(
        "cars/search.html",
        {"request": request, "cars": filtered_cars, "car_name": car_name},
    )

@router.get("/cars/new", response_class=HTMLResponse)
async def new_car_form(request: Request):
    """Display the form for adding a car"""
    return templates.TemplateResponse("cars/new.html", {"request": request})

@router.post("/cars/new")
async def add_new_car(name: str = Form(...), year: int = Form(...)):
    """Handler for saving a new car and redirecting to the list"""
    add_car(name, year)
    return RedirectResponse(url="/cars", status_code=303)

@router.get("/cars", response_class=HTMLResponse)
async def list_cars(request: Request):
    """Displays a list of all cars"""
    return templates.TemplateResponse("cars/list.html", {"request": request, "cars": get_cars()})
