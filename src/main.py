from fastapi import FastAPI
from src.api.v1 import jobs as job_endpoints
from src.core.database import SessionLocal, engine
from src.models.jobs import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(job_endpoints.router, prefix="/jobs", tags=["jobs"])
#app.include_router(job_endpoints.router, prefix="")