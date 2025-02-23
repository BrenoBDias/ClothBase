
from ..database import Base
from sqlalchemy import Column, DateTime, Integer, VARCHAR

class UserType(Base):
    __tablename__ = "usertype"

    id  = Column(Integer, primary_key=True, index=True)
    type_name = Column(VARCHAR(20), nullable=False)