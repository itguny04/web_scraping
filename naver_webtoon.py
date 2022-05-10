import requests
from bs4 import BeautifulSoup

day = ["mon","tue","wed","thu","fri","sat","sun"]
webtoon_contents = []

for i in day:
    url = f"https://comic.naver.com/webtoon/weekdayList?week={i}"

    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    data = soup.select('#content > div.list_area.daily_img > ul > li')
    webtoon_count = len(data)

    tmp = list()

    for j in range(1, webtoon_count):
        tmp.append(data[j].find('dt').find('a').get_text())
    webtoon_contents.append(tmp)

print(webtoon_contents)