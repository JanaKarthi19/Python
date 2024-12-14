import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

email = EmailMessage()

# Email contacts and contents

html    = Template(Path('index.html').read_text())

email['from'] = 'Mr.Loki'
email['to'] = 'receiver@gamail.com'
email['subject'] = 'Subject of mail'

content = "Text Messages Here"

# Text Content

email.set_content(content)

# HTML Content

email.set_content(html.substitute({'content' : 'contents'}),'html')

 # Send email through smtp


with smtplib.SMTP(host='smtp.gmail.com', port=587) as stmp:
    stmp.ehlo()
    stmp.starttls()
    stmp.login(user="sender@gmail.com",password='password')
    stmp.send_message(email)
    print('all good boss')
    # stmp.quit()