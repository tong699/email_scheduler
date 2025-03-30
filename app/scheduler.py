from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import uuid
from app.postmark_client import send_email

scheduler = BackgroundScheduler()
scheduler.start()

def _job_function(recipient: str, subject: str, message: str):
    print(f"[JOB] Attempting to send email to {recipient}")
    try:
        send_email(recipient, subject, message)
        print("[JOB] Email sent successfully")
    except Exception as e:
        print("[JOB] ERROR sending scheduled email:", e)

def schedule_email(recipient: str, subject: str, message: str, send_at: datetime) -> str:
    job_id = str(uuid.uuid4())

    try:
        scheduler.add_job(
            _job_function,
            trigger="date",
            run_date=send_at,
            args=[recipient, subject, message],
            id=job_id,
            replace_existing=True
        )
        print(f"[SCHEDULER] Scheduled job {job_id} for {send_at}")
        return job_id
    except Exception as e:
        print("[SCHEDULER] ERROR scheduling job:", e)
        raise
