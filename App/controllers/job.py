from App.models import Job
from App.database import db

def get_all_jobs():
    return Job.query.all()

def get_all_jobs_json():
    jobs = get_all_jobs()
    return [jobs.get_json() for job in jobs]
