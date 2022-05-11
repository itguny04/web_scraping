
import requests
from bs4 import BeautifulSoup
import pandas as pd

articles = list()

for i in range(5459000, 5459005):
    try:
        url = f'https://news.kbs.co.kr/news/view.do?ncd={i}'
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')

        title_selector = '#content > div > div.detail-component.det-news > div.landing-box > div.landing-caption > h5'
        title = soup.select_one(title_selector).get_text()

        articles.append(title)

    except:
        continue

pd.DataFrame({'기사 제목':articles}).to_csv("articles.csv", encoding="utf-8-sig", header=False, index=False)

