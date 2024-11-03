import smtplib
from email.message import EmailMessage

email = EmailMessage()

email['from'] = 'Mr.Loki'
email['to'] = 'justforfunsodontangry@gmail.com'
email['subject'] = 'Declaration of war'

email.set_content('This is warland. The mighty kingdom of Elbaf. They say it is the birthplace of war. And I am sun god who will bring about the end of the world.  LOKI')

with smtplib.SMTP(host='stmp.gmail.com', port=587) as stmp:
    stmp.ehlo()
    stmp.starttls()
    stmp.login('joyboy.elphaba.2024@gmail.com','OnePiece#24')
    stmp.send_message(email)
    print('all good boss')
    # stmp.quit()