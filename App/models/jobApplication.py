from App.database import db
from .user import User
from .job import Job
from datetime import datetime, timezone

def get_utc_time():
    return datetime.now(timezone.utc)

class JobApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    applicant_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)
    date = db.Column(db.DateTime, default=get_utc_time)
    status = db.Column(db.String(20), default='pending')

    # Define relationships for convenience
    job = db.relationship('Job', backref='applications')
    applicant = db.relationship('User', backref='applications')

    def __repr__(self):
        return f'<JobApplication id:{self.id} - applicant_id:{self.applicant_id} - job_id:{self.job_id}>'

    def is_approved(self):
        return self.status == 'approved'

    def withdraw_application(self):
        db.session.delete(self)
        db.session.commit()

    def get_job(self):
        return self.job  # Leverage relationship to fetch job

    def num_days_submitted(self):
        if self.date:
            return (datetime.now(timezone.utc) - self.date).days
        return None
