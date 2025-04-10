from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from src.core.database import Base
from pydantic import BaseModel

class Jobs(Base):               # this is the sqlalchemy model for database operations
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    company = Column(String, default="")
    description = Column(String, default="")
    url = Column(String, default="")

class Jobs_Pydantic(BaseModel):
    id: int
    title: str
    company: str
    description: str
    url: str

    class Config:
        orm_mode = True
