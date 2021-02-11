import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Email Account
email_sender_account = "jobs@olebause.de"
email_sender_username = "jobs@olebause.de"
email_sender_password = "3Lfl*01r"
email_smtp_server = "olebause.de"
email_smtp_port = 465

#Email Content
email_recepients = ["info@bausecreative.de"]
email_subject = "Test"
email_body = "Test Email."

#login to email server
server = smtplib.SMTP(email_smtp_server,email_smtp_port)
server.starttls()
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
    server.sendmail(email_sender_account,recipient,text)

#All emails sent, log out.
server.quit()
