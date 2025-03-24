from fastapi import APIRouter, Form, Response, Request
import json

router = APIRouter()

@router.post("/items")
def add_to_cart(response: Response, request: Request, flower_id: int = Form(...)):
    """Adds flower to the cart (cookie)"""

    cart_cookie = request.cookies.get("cart")
    print(f"🔍 Cookies received: {cart_cookie}")

    cart = json.loads(cart_cookie) if cart_cookie else []
    print(f"📦 Cart data: {cart}")

    cart.append(flower_id)
    response.set_cookie(key="cart", value=json.dumps(cart), httponly=True)

    print(f"✅ Cart updated (POST): {cart}")
    return {"message": "Flower added to cart", "cart": cart}

@router.get("/items")
def get_cart(request: Request):
    """Returns the cart of user"""
    cart_cookie = request.cookies.get("cart")
    print(f"🔍 Cookies received: {cart_cookie}")

    cart = json.loads(cart_cookie) if cart_cookie else []
    print(f"📦 Cart data: {cart}")

    return {"cart": cart}
