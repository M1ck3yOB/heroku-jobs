import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class SendMail:
    def __init__(self):
        self.email_sender_account = "cron@bausecreative.de"
        self.email_sender_username = "cron@bausecreative.de"
        self.email_sender_password = "Ruamzuzla9078#"
        self.email_smtp_server = "mail.bausecreative.de"
        self.email_smtp_port = 465

    def send_mail(self, email_subject, email_body, email_recepients):
        # login to email server
        context = ssl.create_default_context()
        server = smtplib.SMTP_SSL(self.email_smtp_server, self.email_smtp_port, context=context)
        # server.starttls()
        server.login(self.email_sender_username, self.email_sender_password)

        for recipient in email_recepients:
            print(f"Sending email to {recipient}")
            message = MIMEMultipart('alternative')
            message['From'] = self.email_sender_account
            message['To'] = recipient
            message['Subject'] = email_subject
            message.attach(MIMEText(email_body, 'html'))
            text = message.as_string()
            server.sendmail(self.email_sender_account, recipient, text)

        # All emails sent, log out.
        server.quit()

