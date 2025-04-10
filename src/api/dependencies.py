from fastapi import Depends
from sqlalchemy.orm import Session
from src.core.database import get_db
from src.services.job_service import JobService

def get_job_service(db: Session = Depends(get_db)) -> JobService:
    return JobService(db)