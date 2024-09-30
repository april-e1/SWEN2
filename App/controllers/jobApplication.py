from App.database import db
from App.models import JobApplication

def withdraw_application(application_id):
    try:
        application = JobApplication.query.get(application_id)
        if application:
            application.withdraw_application()
            return True
        return False
    except Exception as e:
        print(f"Error withdrawing application: {e}")
        return False

def get_job_for_application(application_id):
    try:
        application = JobApplication.query.get(application_id)
        if application:
            return application.get_job()
        return None
    except Exception as e:
        print(f"Error retrieving job for application: {e}")
        return None
    
def days_submitted(application_id):
    try:
        application = JobApplication.query.get(application_id)
        if application:
            return application.num_days_submitted
    except Exception as e:
        print(f"Error calaculating number of days application was submitted:{e}")
        return None
