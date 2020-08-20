import os
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from time import sleep
from random import randint

# from utils.mail_templates import TEMPLATES

SMTP_SERVER = 'smtp.gmail.com'
PORT = 465
SENDER = 'predictablebot@gmail.com'
PASSWORD = 'SekSI2019'

default_subject = 'Hello!'
default_content = 'Hello from predictable!'

code = 123456

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


def send_confirmation_mail(recipient):
    global code
    code = randint(100000, 999999)
    send_email(recipient, content=str(code))
