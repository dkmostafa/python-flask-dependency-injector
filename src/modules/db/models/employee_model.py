from dataclasses import dataclass

from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER

from sqlalchemy.orm import declarative_base

Base = declarative_base()
tableName = "employee"


@dataclass
class EmployeeModel(Base):
    __tablename__ = tableName

    id: int = Column(INTEGER(11), primary_key=True)
    name: str = Column(String(255))
    username: str = Column(String(255), unique=True)
    email: str = Column(String(255), unique=True)
