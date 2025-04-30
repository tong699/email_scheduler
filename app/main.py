from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime, timezone
from app.scheduler import schedule_email
from app.postmark_client import send_email

app = FastAPI()

class EmailScheduleRequest(BaseModel):
    recipient: str
    subject: str
    message: str
    send_at: Optional[datetime] = None

@app.post("/schedule-email")
def schedule_email_endpoint(request: EmailScheduleRequest):
    print("[API] Schedule request:", request.dict())

    if request.send_at <= datetime.now(timezone.utc):
        raise HTTPException(status_code=400, detail="send_at must be a future time")

    try:
        job_id = schedule_email(
            recipient=request.recipient,
            subject=request.subject,
            message=request.message,
            send_at=request.send_at
        )
        return {"job_id": job_id, "message": "Email scheduled successfully"}
    except Exception as e:
        print("[API] ERROR scheduling email:", e)
        raise HTTPException(status_code=500, detail="Failed to schedule email. Check logs.")


@app.post("/send-now")
def send_now(request: EmailScheduleRequest):
    try:
        send_email(
            recipient=request.recipient,
            subject=request.subject,
            message=request.message
        )
        return {"message": "Email sent immediately"}
    except Exception as e:
        print("Send now error:", e)
        raise HTTPException(status_code=500, detail=str(e))
