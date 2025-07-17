from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Book Service",
    description="REST API для управления книгами",
    version="1.0.0"
)

class Book(BaseModel):
    id: int
    title: str
    author: str
    price: float
    stock: int
    
books_db = [
    Book(id=1, title="Clean Code", author="Robert C. Martin", price=29.99, stock=10),
    Book(id=2, title="1984", author="George Orwell", price=15.50, stock=5)
]

@app.get("/books", response_model=list[Book])
def get_books():
    return books_db

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    book = next((b for b in books_db if b.id == book_id), None)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

