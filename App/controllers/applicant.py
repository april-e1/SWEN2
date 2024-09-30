from App.models import job, jobApplication

def view_job(applicant):
    try:
        return applicant.view_job()
    except Exception as e:
        print(f"Error viewing jobs: {e}")
        return None

def apply_to_job(applicant, job_id):
    try:
        return applicant.apply_to_job(job_id)
    except Exception as e:
        print(f"Error applying to job: {e}")
        return None