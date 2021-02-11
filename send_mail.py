import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Email Account
email_sender_account = "cron@bausecreative.de"
email_sender_username = "cron@bausecreative.de"
email_sender_password = "Ruamzuzla9078#"
email_smtp_server = "mail.bausecreative.de"
email_smtp_port = 465

#Email Content
email_recepients = ["info@bausecreative.de", "olebause@hotmail.de"]
email_subject = "Test"
email_body = "Test Email."

#login to email server
context = ssl.create_default_context()
server = smtplib.SMTP_SSL(email_smtp_server, email_smtp_port, context=context)
#server.starttls()
server.login(email_sender_username, email_sender_password)

#For loop, sending emails to all email recipients
for recipient in email_recepients:
    print(f"Sending email to {recipient}")
    message = MIMEMultipart('alternative')
    message['From'] = email_sender_account
    message['To'] = recipient
    message['Subject'] = email_subject
    message.attach(MIMEText(email_body, 'html'))
    text = message.as_string()
    server.sendmail(email_sender_account, recipient, text)

#All emails sent, log out.
server.quit()
