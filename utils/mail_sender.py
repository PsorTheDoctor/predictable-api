import os
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from time import sleep




SMTP_SERVER = 'smtp.gmail.com'
PORT = 465
SENDER = os.environ['PREDICTABLE_EMAIL']
PASSWORD = os.environ['PREDICTABLE_PASSWORD']

default_subject = 'Hello!'
default_content = 'Hello from predictable!'

context = ssl.create_default_context()


def send_email(recipients,
               subject=default_subject,
               content=default_content):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = SENDER
    msg.attach(MIMEText(content, 'plain'))

    with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=context) as server:
        server.login(SENDER, PASSWORD)
        if isinstance(recipients, list):
            for recipient in recipients:
                server.sendmail(SENDER, recipient, msg.as_string())
        else:
            server.sendmail(SENDER, recipients, msg.as_string())


def send_email_repeatedly(recipients,
                          period,
                          subject=default_subject,
                          content=default_content):
    while True:
        send_email(recipients, subject, content)
        sleep(period)
