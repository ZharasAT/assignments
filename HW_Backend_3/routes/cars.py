from fastapi import APIRouter, Request, Query
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from repositories.cars import filter_cars_by_name

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/cars/search", response_class=HTMLResponse)
async def search_cars(request: Request, car_name: str = Query("", alias="car_name")):
    filtered_cars = filter_cars_by_name(car_name) if car_name else []
    return templates.TemplateResponse(
        "/cars/search.html",
        {"request": request, "cars": filtered_cars, "car_name": car_name},
    )
