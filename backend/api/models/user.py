from ..database import Base
from .usertype import UserType
from sqlalchemy import Column, DateTime, Integer, VARCHAR, ForeignKey

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(VARCHAR(50), unique=True, nullable=False)
    email = Column(VARCHAR(50), unique=True, nullable=False)
    password = Column(VARCHAR(50), nullable=False)
    cpf = Column(VARCHAR(50), unique=True, nullable=True)
    cnpj = Column(VARCHAR(50), unique=True, nullable=True)
    user_type = Column(Integer, ForeignKey(UserType.id), nullable=False)