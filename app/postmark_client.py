import requests

POSTMARK_API_URL = "https://api.postmarkapp.com/email"
POSTMARK_SERVER_TOKEN = "0ecbb6dd-d9a3-4f99-9a63-53701b0e1f45"

def send_email(recipient: str, subject: str, message: str):
    payload = {
        "From": "tongcm-wm22@student.tarc.edu.my",
        "To": recipient,
        "Subject": subject,
        "TextBody": message,
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "X-Postmark-Server-Token": POSTMARK_SERVER_TOKEN,
    }
    response = requests.post(POSTMARK_API_URL, json=payload, headers=headers)
    if response.status_code != 200:
        # Log error or retry as needed
        print("Error sending email:", response.text)
    else:
        print("Email sent successfully!")
