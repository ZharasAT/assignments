cars = [
        {"id": 1, "name": "Toyota Camry", "year": 2020},
        {"id": 2, "name": "Ford Focus", "year": 2018},
        {"id": 3, "name": "Tesla Model S", "year": 2022},
        {"id": 4, "name": "Chevrolet Camaro", "year": 2019},
        {"id": 5, "name": "Opel Astra", "year": 2017}
    ]

def get_cars():
    """Returns a list of all cars"""
    return cars

def filter_cars_by_name(car_name: str):
    """Filters cars by name"""
    return [car for car in cars if car_name.lower() in car["name"].lower()]

def add_car(name: str, year: int):
    """Adds a new car to the list"""
    new_id = max(car["id"] for car in cars) + 1 if cars else 1
    cars.append({"id": new_id, "name": name, "year": year})
