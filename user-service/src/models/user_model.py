from sqlalchemy import MetaData, Column, String, Integer
from src.database.db import Base

metadata = MetaData()


class UserModel(Base):
    __tabelname__ = "users"
    __metadata__ = metadata
    id = Column(Integer, primary_key=True, index=True)
    login = Column(String(length=255), nullable=False)
    password = Column(String(length=255), nullable=False)