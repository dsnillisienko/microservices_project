from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    author: str
    price: float
    stock: int

class BookOut(BookCreate):
    id: int
    class Config:
        orm_mode = True