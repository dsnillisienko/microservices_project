from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Order Service",
    description="REST API для оформления заказов",
    version="1.0.0"
)

class Order(BaseModel):
    id: int
    user_id: int
    book_id: int
    quantity: int
    status: str = "created"

orders_db: List[Order] = []

@app.post("/orders", response_model=Order)
def create_order(order: Order):
    orders_db.append(order)
    return order

@app.get("/orders/{order_id}", response_model=Order)
def get_order(order_id: int):
    order = next((o for o in orders_db if o.id == order_id), None)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@app.get("/orders", response_model=List[Order])
def get_orders():
    return orders_db
