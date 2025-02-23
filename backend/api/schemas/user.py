from pydantic import BaseModel
from sqlalchemy import Column, VARCHAR, Integer


class User(BaseModel):
    id: int
    name: str
    email : str