from sqlalchemy import Column, Boolean, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String, unique=True, nullable=False)
    password = Column(String)