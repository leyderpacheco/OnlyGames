import requests
from bs4 import BeautifulSoup

r = requests.get('https://store.steampowered.com/')
soup = BeautifulSoup(r.text, 'lxml')
