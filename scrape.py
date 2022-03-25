import requests
from bs4 import BeautifulSoup

url = 'https://www.odakyu.jp/station/'
res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")
elems = soup.find_all(class_="icon-station")

with open('stations.txt', mode='w', encoding='utf-8') as f:
    for elem in elems:
        f.write(elem.text+'\n')