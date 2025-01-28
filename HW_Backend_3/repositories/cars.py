def get_cars():
    return [
        {"id": 1, "name": "Toyota Camry"},
        {"id": 2, "name": "Ford Focus"},
        {"id": 3, "name": "Tesla Model S"},
        {"id": 4, "name": "Chevrolet Camaro"},
        {"id": 5, "name": "Opel Astra"}
    ]

def filter_cars_by_name(car_name: str):
    cars = get_cars()
    return [car for car in cars if car_name.lower() in car["name"].lower()]
