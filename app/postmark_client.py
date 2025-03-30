import requests

POSTMARK_API_URL = "https://api.postmarkapp.com/email"
POSTMARK_SERVER_TOKEN = "YOUR_POSTMARK_SERVER_TOKEN"

def send_email(recipient: str, subject: str, message: str):
    payload = {
        "From": "your_email@example.com",
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
