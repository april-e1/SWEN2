```python
# inside wsgi.py

'''
Employer Commands
'''

employer_cli = AppGroup('employer', help='Employer object commands')

@employer_cli.command("create-job", help="Create a job as an employer")
@click.argument("employer_id", type=int)
@click.argument("title")
@click.argument("description")
def create_job_command(employer_id, title, description):
    employer_instance = User.query.get(employer_id)  # Assuming Employer inherits from User
    if employer_instance:
        new_job = Job(title=title, description=description, employer_id=employer_instance.id)
        db.session.add(new_job)
        db.session.commit()
        print(f"Job created: {new_job.title} (ID: {new_job.id})")
    else:
        print(f"Employer not found.")



@employer_cli.command('view-applicant', help="View applicants for a job")
@click.argument("job_id", type=int)
def view_applicant_command(job_id):
    applicants = view_applicant(job_id)
    if applicants:
        for app in applicants:
            print(f"Applicant ID: {app.applicant_id}, Status: {app.status}")
    else:
        print(f"No applicants found or employer mismatch.")

app.cli.add_command(employer_cli)

'''
Applicant Commands
'''

applicant_cli = AppGroup('applicant', help="Applican object commands")


@applicant_cli.command("apply", help="Apply to job")
@click.argument("applicant_id", type=int)
@click.argument("job_id", type=int)
def apply_to_job_command(applicant_id, job_id):
    applicant_instance = Applicant.query.get(applicant_id)  # Accessing the Applicant model
    if applicant_instance:
        job_instance = Job.query.get(job_id)  # Fetch the job instance
        if job_instance:
            application = applicant_instance.apply_to_job(job_id)
            if application:
                print(f"Applicant {applicant_id} applied to job {job_id}")
            else:
                print(f"Application failed.")
        else:
            print(f"Job not found.")
    else:
        print(f"Applicant not found.")


app.cli.add_command(applicant_cli)

'''
Job Commands
'''

job_cli = AppGroup('job', help="Job object commands")

@job_cli.command("view-job", help="View all jobs")
def view_job_command():
    jobs = Job.query.all()
    if jobs:
        for job_instance in jobs:
            print(f"Job ID: {job_instance.id}, Title: {job_instance.title}")
    else:
        print(f"No jobs available.")

app.cli.add_command(job_cli)

```

Then execute the command invoking with flask cli with command name and the relevant parameters

flask employer create-job <employer_id> <title> <description>

flask employer view-applicant <job_id>

flask applicant apply <applicant_id> <job_id>

flask job view-job
