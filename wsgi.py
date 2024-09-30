import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import User, Employer, Applicant, Job, JobApplication
from App.main import create_app
from App.controllers import *
# ( create_user, get_all_users_json, get_all_users, initialize, create_job, view_applicant, days_submitted )


# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli

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

'''
JobApplication Commands
'''





'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)