import smtplib
from email.mime.text import MIMEText
from string import Template
from pathlib import Path  # os.path

html = Template(Path('./index.html').read_text())
# for zoho mail!
# defy to/from
sender = 'example@zohomail.eu'
recipient = 'email1@email.com; email2@email.com; email3@email.com; email4@email.com'

# create message
msg = 'The message from your email'
msg['Subject'] = 'Here is the subject of the email'  # subject
msg['From'] = sender
msg['To'] = recipient

# Create server object with SSL option
server = smtplib.SMTP_SSL('smtp.zoho.eu', 465)

# Perform operations via server
server.login('example@zohomail.eu', 'password')
server.sendmail(sender, ['email1@email.com','email2@email.com', 'email3@email.com','email4@email.com'], msg.as_string())
server.quit()
print('Work done boss!')
