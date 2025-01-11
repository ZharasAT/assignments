from fastapi import FastAPI, HTTPException

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

@app.get("/cars/{car_id}")
def get_car_by_id(car_id: int):
    car = next((car for car in cars if car["id"] == car_id), None)

    if car is None:
        raise HTTPException(status_code=404, detail="Not found")
    return car