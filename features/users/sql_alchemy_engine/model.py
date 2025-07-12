from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, String

Base = DeclarativeBase()

class Users(Base):
    __tablename__ = "usuarios"
    name = Column(String(10))