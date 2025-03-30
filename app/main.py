from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime, timedelta
from app.scheduler import schedule_email

app = FastAPI()

class EmailScheduleRequest(BaseModel):
    recipient: str
    subject: str
    message: str
    send_at: datetime  # ISO formatted date-time when the email should be sent

@app.post("/schedule-email")
def schedule_email_endpoint(request: EmailScheduleRequest):
    # Validate that the send time is in the future
    if request.send_at <= datetime.utcnow():
        raise HTTPException(status_code=400, detail="send_at must be a future time")

    job_id = schedule_email(
        recipient=request.recipient,
        subject=request.subject,
        message=request.message,
        send_at=request.send_at
    )
    return {"job_id": job_id, "message": "Email scheduled successfully"}
