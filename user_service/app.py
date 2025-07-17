from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title= "User service",
    description="REST API для управления пользователями",
    version="1.0.0"
)

class User(BaseModel):
    id: int
    name: str
    email: str
    
users_db = [
    User(id=1, name="Max", email="max@example.com"),
    User(id=2, name="Oleg", email="oleg@example.com")
]

@app.get("/users", response_model=list[User])
def get_users():
    return users_db

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    user = next((u for u in users_db if u.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
