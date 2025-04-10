from fastapi import APIRouter, Depends, HTTPException
from typing import List
from src.models.jobs import Jobs_Pydantic
from src.api.dependencies import get_job_service
from src.services.job_service import JobService

router = APIRouter()

@router.post("/", response_model=Jobs_Pydantic)
def create_job(
    title: str,
    description: str,
    job_service: JobService = Depends(get_job_service)
):
    return job_service.create_job(title=title, description=description)

@router.get("/", response_model=List[Jobs_Pydantic])
def read_jobs(
    skip: int = 0,
    limit: int = 500,
    job_service: JobService = Depends(get_job_service)
):
    return job_service.get_jobs(skip=skip, limit=limit)

@router.get("/{job_id}", response_model=Jobs_Pydantic)
def read_job(
    job_id: int,
    job_service: JobService = Depends(get_job_service)
):
    job = job_service.get_job(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="job not found")
    return job_service.get_job(job_id)
