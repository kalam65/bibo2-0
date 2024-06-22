from fastapi import FastAPI, Depends, HTTPException, Request, Form
from sqlalchemy.orm import Session
from typing import List

import models
import schemas
import crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/job/", response_model=schemas.Job)
def create_job(
    request: Request,
    db: Session = Depends(get_db),
    company_name: str = Form(...),
    job_title: str = Form(...),
    industry: str = Form(...),
    job_description: str = Form(...),
    experience: str = Form(...),
    package_upto: str = Form(...),
    skills: str = Form(...),
    location: str = Form(...),
    job_type: str = Form(...),
    email: str = Form(...)
):
    job_data = schemas.JobCreate(
        company_name=company_name,
        job_title=job_title,
        industry=industry,
        job_description=job_description,
        experience=experience,
        package_upto=package_upto,
        skills=skills,
        location=location,
        job_type=job_type,
        email=email
    )
    return crud.create_job(db=db, job=job_data)

@app.get("/", response_model=List[schemas.Job])
def read_jobs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    jobs = crud.get_jobs(db, skip=skip, limit=limit)
    return jobs

@app.get("/job/{job_id}", response_model=schemas.Job)
def read_job(job_id: int, db: Session = Depends(get_db)):
    db_job = crud.get_job(db, job_id=job_id)
    if db_job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return db_job

@app.put("/job/{job_id}", response_model=schemas.Job)
def update_job(job_id: int, job: schemas.JobUpdate, db: Session = Depends(get_db)):
    db_job = crud.get_job(db, job_id=job_id)
    if db_job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return crud.update_job(db=db, job=db_job, job_update=job)

@app.delete("/job/{job_id}", response_model=schemas.Job)
def delete_job(job_id: int, db: Session = Depends(get_db)):
    db_job = crud.get_job(db, job_id=job_id)
    if db_job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return crud.delete_job(db=db, job=db_job)
