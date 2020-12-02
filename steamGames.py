import requests
from bs4 import BeautifulSoup

payload={"appid":584220}
response = requests.get("https://api.rawg.io/api/games")

data=(response.json())

#print(data.values())







