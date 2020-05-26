import smtplib, ssl
from email.mime.text import MIMEText


port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "aledroggo@gmail.com"  # Enter your address
receiver_email = "jarilio99@gmail.com"  # Enter receiver address
import urllib.parse
def data_to_href(data):
    id = data['id']
    name = data['name']
    print(type(name))
    banned_letters = '\.[]{}()<>*+-=!?^$|/' + "\'\"\\"
    for letter in banned_letters:
        print(letter)
        name = name.replace(letter, " ")

    print(name)
    name = name.lower()
    adres = name.replace(" ", "-")

    print(adres)
    default = 'allegro.pl/oferta/'
    url = default + adres + '-' + id
    print(url)
    return url

def send_mail(data, receiver_email, price_threshold):
    context = ssl.create_default_context()

    url = data_to_href(data)

    msg = MIMEText('W serwisie Allegro pojawił się nowy przedmiot w cenie która cię interesuje.\n'
                   '{} w cenie {}\n'
                   '{}'.format(data['name'],data['amount'],url))

    msg['Subject'] = 'Znaleziono przedmiot którego poszukujesz'
    msg['From'] = 'Aledroggo'
    msg['To'] = receiver_email

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        print('login')
        server.login(sender_email, password)
        print('sendmail')
        server.sendmail(sender_email, receiver_email, msg.as_string())