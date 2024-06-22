from pydantic import BaseModel
from typing import Optional

class JobBase(BaseModel):
    company_name: str
    job_title: str
    industry: str
    job_description: str
    experience: str
    package_upto: str
    skills: str
    location: str
    job_type: str
    email: str

class JobCreate(JobBase):
    pass

class Job(JobBase):
    id: int

    class Config:
        orm_mode: True

class JobUpdate(BaseModel):
    company_name: Optional[str] = None
    job_title: Optional[str] = None
    industry: Optional[str] = None
    job_description: Optional[str] = None
    experience: Optional[str] = None
    package_upto: Optional[str] = None
    skills: Optional[str] = None
    location: Optional[str] = None
    job_type: Optional[str] = None
    email: Optional[str] = None
