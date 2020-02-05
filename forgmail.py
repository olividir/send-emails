import smtplib
from email.message import EmailMessage

# 1 Log into Gmail with your account
# 2 Navigate to https://security.google.com/settings/security/apppasswords
# 3 In "select app" choose "custom", give it an arbritary name
# 4 It will give you 16 chars token

# Use the token as password in combination with your full Gmail account and two factor authentication will not be required

email = EmailMessage()
email['from'] = 'Name of sender'
email['to'] = 'example@example.com'
email['subject'] = 'Subject of the email'

email.set_content('Message of email')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('account@gmail.com', 'password')
    smtp.send_message(email)
    print('All good mr Boss!')
