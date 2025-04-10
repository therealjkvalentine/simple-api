from typing import List
from sqlalchemy.orm import Session
from src.models.jobs import Jobs

class JobService:
    def __init__(self, db: Session):
        self.db = db

    def create_job(self, title: str, description: str) -> Jobs:
        db_job = Jobs(title=title, description=description)
        self.db.add(db_job)
        self.db.commit()
        self.db.refresh(db_job)
        return db_job

    def get_jobs(self, skip: int = 0, limit: int = 500) -> List[Jobs]:
        return self.db.query(Jobs).offset(skip).limit(limit).all()
    
    def get_job(self, task_id: int) -> Jobs:
        return self.db.query(Jobs).filter(Jobs.id == task_id).first()
    