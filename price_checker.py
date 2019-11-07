import requests
from bs4 import BeautifulSoup
import smtplib
import time

#URL = 'https://www.amazon.com/MSI-GeForce-GTX-1660-Ti/dp/B07N824KNV/ref=sr_1_1?qid=1572962463&rnid=17923671011&s=computers-intl-ship&sr=1-1'

# Link til produktet du vil sjekke pris på.
URL = input("Link to product: ")

# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36

def check_price():

    # User Agent til nettleseren (søk etter My User Agent på google)
    user_agent = input("Browser User-Agent: ")
    headers = {'User-Agent': user_agent}
    
    page = requests.get(URL, headers = headers)

    
    soupTemp = BeautifulSoup(page.content, 'html.parser')
    soup = BeautifulSoup(soupTemp.prettify(), 'html.parser')

    title = soup.find(id = 'productTitle').get_text()
    price = soup.find(id = 'priceblock_ourprice').get_text()
    converted_price = float(price[1:7])


    print(title.strip())
    print(converted_price)

    # Sett pris grense
    # TODO - sett pris med input
    if (converted_price < 200.00):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    sender = input("Send e-mail from: ")

    server.login(sender, 'tfypmpbytubezxls')
    subject = 'Prisen har falt!'
    body = 'Sjekk Amazon link: ' + URL

    sender = input("Send e-mail from: ")
    reciever = input("Send e-mail to: ")

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        sender,
        reciever,
        msg
        )

    print('E-mail has been sent!')
    server.quit()


#while(True):
#    check_price()
#    time.sleep(60)

check_price()
