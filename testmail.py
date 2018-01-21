import smtplib
from pswd import password #pswd is a hidden .py with password='my password'

def notify():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('p2lgw2@gmail.com',password)

    message = 'AT TEMP'

    server.sendmail('p2lgw2@gmail.com','p2lgw2@gmail.com',message)
    server.quit()

notify()

