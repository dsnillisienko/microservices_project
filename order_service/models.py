from sqlalchemy import Column, Integer, Enum
from .database import Base
import enum

class OrderStatus(str, enum.Enum):
    created = "created"
    paid = "paid"
    shipped = "shipped"

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    book_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    status = Column(Enum(OrderStatus), default=OrderStatus.created)