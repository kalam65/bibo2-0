from sqlalchemy import Column, Integer, String
from database import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, index=True)
    job_title = Column(String, index=True)
    industry = Column(String, index=True)
    job_description = Column(String, index=True)
    experience = Column(String, index=True)
    package_upto = Column(String, index=True)
    skills = Column(String, index=True)
    location = Column(String, index=True)
    job_type = Column(String, index=True)
    email = Column(String, index=True)
