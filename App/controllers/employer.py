from App.models import Job, JobApplication
from App.database import db

def create_job(employer, title, description):
    try:
        return employer.create_job(title, description)
    except Exception as e:
        print(f"Error creating job: {e}")
        return None

def view_applicant(job_id):
    # Fetch all job applications related to the specific job
    return JobApplication.query.filter_by(job_id=job_id).all()

