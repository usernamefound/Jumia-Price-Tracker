import requests
from bs4 import BeautifulSoup
import lxml
import re



url = 'https://www.jumia.ma/edifier-x2-tws-ecouteurs-ecouteurs-sans-fil-bluetooth-5.1-assistant-vocal-pilote-13-mm-controle-tactile-jusqua-28-heures-de-jeu-mode-de-jeu-42704104.html'
# url = 'https://www.ebay.com/itm/364034118840?_trkparms=amclksrc%3DITM%26aid%3D777008%26algo%3DPERSONAL.TOPIC%26ao%3D1%26asc%3D20220725101321%26meid%3D666c47ec23204bcda04921c16d81aab4%26pid%3D101251%26rk%3D1%26rkt%3D1%26itm%3D364034118840%26pmt%3D0%26noa%3D1%26pg%3D2380057%26algv%3DPersonalizedTopicsV2WithTopicMLR%26brand%3DApple&_trksid=p2380057.c101251.m47269&_trkparms=pageci%3Abbf046cb-5ae5-11ed-b87f-1efbc5a79902%7Cparentrq%3A39d8e3a41840a1208baab523fffcb6c0%7Ciid%3A1'

def get_link_data(url):
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
            'Accept-Language': 'en',
        }

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    title = soup.find("h1", class_="-fs20 -pts -pbxs")
    if title != None:
        title = soup.find("h1", class_="-fs20 -pts -pbxs").getText().strip()

    real_price = soup.find("span", class_="-b -ltr -tal -fs24")
    if real_price != None:
        real_price = real_price.getText().strip()

    # clean the price string so we can convert it to a float
        price = re.sub(r'[^\d.]', '', real_price)

        return title, float(price)

# print(get_link_data(url))
