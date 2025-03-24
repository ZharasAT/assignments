from pydantic import BaseModel

class Purchase(BaseModel):
    user_id: int
    flower_id: int