from typing import Any
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from auth_routes import auth_router
from order_routes import order_router

app = FastAPI()

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None

class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None

@app.post('/user/', response_model = UserOut)
async def create_user(user: UserIn) -> Any:
    return user

app.include_router(auth_router)
app.include_router(order_router)