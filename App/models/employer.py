from App.database import db
from .user import User
from .job import Job 
from .jobApplication import JobApplication

class Employer(User):
    def __init__(self, username, password):
        super().__init__(username, password)
    
    # def create_job(self, title, description):
    #     new_job = Job(employer_id=self.id, title=title, description=description)
    #     db.session.add(new_job)
    #     db.session.commit()
    #     return new_job

    def view_applicant(self,job_id):
        job = Job.query.get(job_id)
        if job and job.employer_id == self.id:
            applications = JobApplication.query.filter_by(job_id=job_id).all()
            return applications
        else:
            return None


    
