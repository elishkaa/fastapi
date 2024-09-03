from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
import smtplib
from email.mime.text import MIMEText

router = APIRouter()

class EmailSchema(BaseModel):
    email: EmailStr
    subject: str
    message: str

@router.post("/send-email/")
async def send_email(email_details: EmailSchema):
    sender_email = "eliran.avihen@gmail.com"
    receiver_email = email_details.email
    subject = email_details.subject
    message = email_details.message
    mailtrap_user = "e4836ed368525b"
    mailtrap_pass = "cce1a6980e721a"

    try:
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = receiver_email

        # Mailtrap SMTP server details
        server = smtplib.SMTP('sandbox.smtp.mailtrap.io', 2525)
        server.starttls()
        server.login(mailtrap_user, mailtrap_pass)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        return {"message": "Email sent successfully to Mailtrap!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send email. Error: {e}")
