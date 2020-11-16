import requests
from bs4 import BeautifulSoup

URL = 'https://store.steampowered.com/app/933110/Age_of_Empires_III_Definitive_Edition/?curator_clanid=35480745'

headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}

page = requests.get(URL,headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

titulo = soup.find("div",{"class":"apphub_AppName"}).get_text()
precio = soup.find("div",{"class":"game_purchase_price price"}).get_text()


print(titulo)
print(precio)