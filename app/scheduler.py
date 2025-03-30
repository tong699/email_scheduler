from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import uuid
from app.postmark_client import send_email

# Create a scheduler instance
scheduler = BackgroundScheduler()
scheduler.start()

def _job_function(recipient: str, subject: str, message: str):
    # Call the function to send email through Postmark
    send_email(recipient, subject, message)

def schedule_email(recipient: str, subject: str, message: str, send_at: datetime) -> str:
    # Generate a unique job id
    job_id = str(uuid.uuid4())
    scheduler.add_job(
        _job_function,
        trigger="date",
        run_date=send_at,
        args=[recipient, subject, message],
        id=job_id
    )
    return job_id
