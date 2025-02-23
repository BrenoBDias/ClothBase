from fastapi import APIRouter
from ..schemas import User

router = APIRouter()

@router.post("/user/")
async def create_user(
    user:User
    ):
    return user