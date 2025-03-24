from pydantic import BaseModel

class Flower(BaseModel):
    id: int
    name: str
    quantity: int
    price: float