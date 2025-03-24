from fastapi import FastAPI
from routes import auth, flowers, cart, purchases
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")

print(f"Loaded SECRET_KEY: {SECRET_KEY}")

app = FastAPI(title="Flower Marketplace")

# Adding of routes
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(flowers.router, prefix="/flowers", tags=["Flowers"])
app.include_router(cart.router, prefix="/cart", tags=["Cart"])
app.include_router(purchases.router, prefix="/purchased", tags=["Purchases"])

import json

print("✅ Загруженные маршруты")
for route in app.routes:
    print(f"{route.path} - {route.methods}")

@app.get("/")
def read_root():
    return {"message": "Welcome to Flower Marketplace!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

print("✅ auth.py загружен")
