from fastapi import APIRouter

router = APIRouter()

@router.get("/greet")
def greet():
    return {"message": "Greetings from a router!"}

@router.get("/greet/{user_name}")
def greet(user_name: str = 'Isai'):
    return {"message": f"Greetings from a router! {user_name}"}