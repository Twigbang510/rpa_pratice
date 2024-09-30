# Chapter 18: Sending Email and Text Messages

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import imaplib
import email

# 1. Sending an Email with smtplib
def send_email(sender_email, sender_password, recipient_email, subject, message):
    try:
        # Setup the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Connecting to Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)

        # Sending the email
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")  # Output: Email sent successfully!
    except Exception as e:
        print(f"Failed to send email: {e}")

# 2. Checking Email Inbox with imaplib
def check_inbox(email_user, email_password):
    try:
        # Connecting to the mail server
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(email_user, email_password)
        mail.select('inbox')

        # Search for all emails in the inbox
        result, data = mail.search(None, 'ALL')
        mail_ids = data[0].split()

        # Fetch the latest email
        latest_email_id = mail_ids[-1]
        result, data = mail.fetch(latest_email_id, '(RFC822)')

        raw_email = data[0][1]
        msg = email.message_from_bytes(raw_email)
        print(f"From: {msg['from']}")  # Output: Sender's email
        print(f"Subject: {msg['subject']}")  # Output: Email subject
        print(f"Body: {msg.get_payload(decode=True)}")  # Output: Email body
    except Exception as e:
        print(f"Failed to check inbox: {e}") 

# 3. Sending Text Messages using Twilio
from twilio.rest import Client

def send_text_message(account_sid, auth_token, from_phone, to_phone, message_body):
    try:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=message_body,
            from_=from_phone,
            to=to_phone
        )
        print(f"Text message sent successfully! SID: {message.sid}")  # Output: Text message sent successfully! SID: <message_sid>
    except Exception as e:
        print(f"Failed to send text message: {e}")  
