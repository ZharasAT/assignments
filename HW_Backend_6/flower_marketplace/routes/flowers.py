from fastapi import APIRouter, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from repo.flowers import FlowersRepository
from models.flower import Flower

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/")
def get_flowers(request: Request):
    """Shows the list of flowers"""
    flowers = FlowersRepository.get_all_flowers()
    return templates.TemplateResponse("flowers/list.html", {
        "request": request,
        "flowers": flowers
    })

@router.post("/")
def add_flower(
        name: str = Form(...),
        quantity: int = Form(...),
        price: float = Form(...)
):
    """Adds flower to the Base"""
    new_flower = Flower(
        id=len(FlowersRepository.flowers) + 1,
        name=name,
        quantity=quantity,
        price=price
    )

    FlowersRepository.add_flower(new_flower)  # Saves in Storage

    return RedirectResponse(url="/flowers", status_code=303)