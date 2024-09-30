from App.database import db
from .user import User

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    employer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Relationship to fetch employer
    employer = db.relationship('User', backref='jobs')

    def __init__(self, title, description, employer_id):
        self.title = title
        self.description = description
        self.employer_id = employer_id

    def __repr__(self):
        return f'<Job id:{self.id} - title:{self.title} - employer_id:{self.employer_id}>'
