from fastapi import APIRouter, Request, Response, HTTPException, Depends
from fastapi.templating import Jinja2Templates
import json
from repo.purchases import PurchasesRepository
from repo.flowers import FlowersRepository
from dependencies import verify_jwt

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.post("/")
def purchase_items(
    request: Request,
    response: Response,
    user_data: dict = Depends(verify_jwt)
):
    """Moves cart items to purchased and clears the cart"""

    cart_cookie = request.cookies.get("cart")
    cart = json.loads(cart_cookie) if cart_cookie else []

    if not cart:
        raise HTTPException(status_code=400, detail="Cart is empty")

    # 1. Checking for the flowers
    for flower_id in cart:
        if not FlowersRepository.get_flower_by_id(flower_id):
            raise HTTPException(status_code=404, detail=f"Flower with ID {flower_id} not found")

    # 2. Adding purchases
    email = user_data.get("sub")
    PurchasesRepository.add_purchases(user_id=email, flower_ids=cart)

    # 3. Cart clearing
    response.delete_cookie("cart")

    return {"message": "Purchase successful", "purchased_ids": cart}

@router.get("/")
def purchased_items(request: Request, user_data: dict = Depends(verify_jwt)):
    """Shows the list of purchased flowers"""
    email = user_data.get("sub")
    flowers = PurchasesRepository.get_purchases_by_user(email)

    return templates.TemplateResponse("purchases/list.html", {
        "request": request,
        "flowers": flowers
    })
