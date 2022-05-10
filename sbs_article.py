import requests
from bs4 import BeautifulSoup

def get_article():
    article_list = list()

    for i in range(1, 11):
        url = f"https://news.sbs.co.kr/news/newsflash.do?plink=GNB&cooper=SBSNEWS&pageIdx={i}"
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        article_count = len(soup.select("#container > div > div.w_news_list.type_issue > ul > li"))

        for j in range(1, article_count+1):
            selector = f"#container > div > div.w_news_list.type_issue > ul > li:nth-child({j}) > a.news > p > strong"
            article_list.append(soup.select(selector)[0].get_text())

    return article_list

if __name__ == '__main__':
    article = get_article()
    for i in range(0,len(article)):
        print(f"{i+1}.{article[i]}")