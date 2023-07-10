from fastapi import APIRouter

order_router = APIRouter(
    prefix='/orders'
)

@order_router.get('/')
async def hello():
    return {"message": "Hello from order router"}