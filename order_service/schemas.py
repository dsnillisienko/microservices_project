from pydantic import BaseModel
from typing import Literal

class OrderCreate(BaseModel):
    user_id: int
    book_id: int
    quantity: int

class OrderOut(OrderCreate):
    id: int
    status: Literal["created", "paid", "shipped"]
    class Config:
        orm_mode = True