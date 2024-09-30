from App.database import db
from .user import User
from .job import Job
from .jobApplication import JobApplication

class Applicant(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    def __repr__(self):
        return f'<Applicant id:{self.id} - username:{self.username}>'

    def view_job(self):
        return Job.query.all()

    def apply_to_job(self, job_id):
        job = Job.query.get(job_id)
        if job:
            new_application = JobApplication(applicant_id=self.id, job_id=job.id)
            db.session.add(new_application)
            db.session.commit()
            return new_application
        else:
            return None
        
        