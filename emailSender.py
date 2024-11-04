import smtplib
from email.message import EmailMessage

email = EmailMessage()

# Email contacts and contents

email['from'] = 'Mr.Loki'
email['to'] = 'hostmail@gmail.com'
email['subject'] = 'Subject of mail'

email.set_content('Contents of email')

 # Send email through smtp


with smtplib.SMTP(host='smtp.gmail.com', port=587) as stmp:
    stmp.ehlo()
    stmp.starttls()
    stmp.login('hostmail@gmail.com','Password#24')
    stmp.send_message(email)
    print('all good boss')
    # stmp.quit()