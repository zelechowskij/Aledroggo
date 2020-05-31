import smtplib, ssl
from email.mime.text import MIMEText


port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "aledroggo@gmail.com"  # Enter your address
password = "Eskalopka1"


def data_to_href(data):
    id = data['id']
    name = data['name']
    banned_letters = '\.[]{}()<>*+-=!?^$|/' + "\'\"\\"
    for letter in banned_letters:

        name = name.replace(letter, " ")


    name = name.lower()
    adress = name.replace(" ", "-")


    default = 'allegro.pl/oferta/'
    url = default + adress + '-' + id

    return url


def send_mail_success(data, receiver_email, price_threshold):
    context = ssl.create_default_context()

    url = data_to_href(data)

    msg = MIMEText('W serwisie Allegro pojawił się nowy przedmiot w cenie która cię interesuje.\n'
                   '{} w cenie {}\n'
                   '{}\n'
                   'Jeżeli jednak nie jest to rzecz która cię interesowała, spróbój jeszcze raz www.aledroggo.pl'.format(data['name'],data['amount'],url))

    msg['Subject'] = 'Znaleziono przedmiot którego poszukujesz'
    msg['From'] = 'Aledroggo'
    msg['To'] = receiver_email

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        print('login')
        server.login(sender_email, password)
        print('sendmail')
        server.sendmail(sender_email, receiver_email, msg.as_string())


def send_mail_failure(data, receiver_email):
    context = ssl.create_default_context()
    msg = MIMEText('Niestety, wyszukiwanie {} które skonfigurowałeś nie zwraca żadnych produktów.\n'
                   'Spróbój jeszcze raz na www.aledroggo.pl\n'.format(data))
    msg['Subject'] = 'Wyszukiwanie nie powiodło się'
    msg['From'] = 'Aledroggo'
    msg['To'] = receiver_email
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        print('login')
        server.login(sender_email, password)
        print('sendmail')
        server.sendmail(sender_email, receiver_email, msg.as_string())