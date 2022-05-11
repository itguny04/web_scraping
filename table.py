import requests
from bs4 import BeautifulSoup

res = requests.get('http://dowellcomputer.com/main.jsp')

soup = BeautifulSoup(res.text, 'html.parser')

table = soup.find_all('table')[1]

infolist = []

# print(table)

for tr in table.find_all("tr"):
    for td in tr.find_all("td"):
        infolist.append(td.get_text())

for i in range(5, len(infolist), 3):
    print(infolist[i])
