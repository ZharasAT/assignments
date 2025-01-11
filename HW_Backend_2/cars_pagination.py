from fastapi import FastAPI

app = FastAPI()

cars = [
    {"id": i, "brand": f"Brand-{i}", "model": f"Model-{i}", "year": 2000 + i % 20}
    for i in range(1, 101)
]

@app.get("/cars")
def get_cars(page: int = 1, limit: int = 10):
    start = (page - 1) * limit
    end = start + limit
    return cars[start:end]