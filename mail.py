
# import the smtplib module. It should be included in Python by default
import smtplib
# set up the SMTP server
# s = smtplib.SMTP(host='smtp.gmail.com', port=587)
# s.starttls()
# s.login('zelechowski.jaroslaw@gmail.com', 'Eskalopka1')


def send_mail(data, mail, price_threshold):
    print(data, mail, price_threshold)