from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import HTMLResponse


app = FastAPI()

cars = [
    {"id": i, "brand": f"Brand-{i}", "model": f"Model-{i}", "year": 2000 + i % 20}
    for i in range(1, 101)
]

class User(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    username: str

users = [
    User(
        id=1,
        email="test@test.com",
        first_name="Aibek",
        last_name="Bekturov",
        username="deadly_knight95"
    ),
User(
        id=2,
        email="marzhan@example.com",
        first_name="Marzhan",
        last_name="Pak",
        username="dark_angel",
    ),
    User(
        id=3,
        email="yermek@nfactorial.com",
        first_name="Yermek",
        last_name="Nurash",
        username="oiboy97",
    ),
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

@app.get("/users", response_class=HTMLResponse)
def get_users():
    html_content = """
    <html>
        <head>
            <title>Users List</title>
        </head>
        <body>
            <h1>Users</h1>
            <table border="1">
                <thead>
                    <tr>
                        <th>Username</th>
                        <th>Name</th>
                    </tr>
                </thead>
                <tbody>
    """

    for user in users:
        user_row = f"""
        <tr>
            <td>{user.username}</td>
            <td>
                <a href="/users/{user.id}">{user.first_name} {user.last_name}</a>
            </td>
        </tr>
        """
        html_content += user_row

    html_content += """
                </tbody>
            </table>
        </body>
    </html>
    """
    return html_content

@app.get("/users/{user_id}", response_class=HTMLResponse)
def get_user_by_id(user_id: int):
    user = next((user for user in users if user.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    html_content = f"""
    <html>
        <head>
            <title>User Details</title>
        </head>
        <body>
            <h1>User Information</h1>
            <ul>
                <li><strong>ID:</strong> {user.id}</li>
                <li><strong>Email:</strong> {user.email}</li>
                <li><strong>First Name:</strong> {user.first_name}</li>
                <li><strong>Last Name:</strong> {user.last_name}</li>
                <li><strong>Username:</strong> {user.username}</li>
            </ul>
            <a href="/users">Back to Users List</a>
        </body>
    </html>
    """
    return html_content