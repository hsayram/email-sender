import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


def create_email():
    html = Template(Path('content.html').read_text())
    email = EmailMessage()
    email['from'] = 'Sender Name'
    email['to'] = '<to email address>'
    email['subject'] = 'This is a subject'
    email.set_content(html.substitute({'param': 'SomeParameter'}), 'html')
    return email


def send_email(email):
    with smtplib.SMTP(host='smtp.gmail.com',
                      port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(user='sender email',
                   password='sender password')
        smtp.send_message(email)
        print('email sent!')


if __name__ == "__main__":
    email = create_email()
    send_email(email)
