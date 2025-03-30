import requests
import os

POSTMARK_API_URL = "https://api.postmarkapp.com/email"
POSTMARK_SERVER_TOKEN = os.getenv("POSTMARK_SERVER_TOKEN")  # Use env variable

def send_email(recipient: str, subject: str, message: str):
    print(f"Sending to: {recipient}, subject: {subject}")
    payload = {
        "From": "your_verified_sender@example.com",
        "To": recipient,
        "Subject": subject,
        "TextBody": message
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "X-Postmark-Server-Token": POSTMARK_SERVER_TOKEN,
    }

    response = requests.post(POSTMARK_API_URL, json=payload, headers=headers)
    print("Postmark response:", response.status_code, response.text)

    if response.status_code != 200:
        raise Exception(f"Failed to send email: {response.text}")
