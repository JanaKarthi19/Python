import smtplib
from email.message import EmailMessage

# Email details and content
email = EmailMessage()

email['from'] = 'Mr.Loki'
email['to'] = 'exmaple@gmail.com'
email['subject'] = 'subject of email'

email.set_content('This is about the content of email')

# Send Mail from host 
with smtplib.SMTP(host='stmp.gmail.com', port=587) as stmp:
    stmp.ehlo()
    stmp.starttls()
    stmp.login('host@gmail.com','Password#24')
    stmp.send_message(email)
    print('all good boss')
    # stmp.quit()
