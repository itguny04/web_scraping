from email import header
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://gall.dcinside.com/board/lists/?id=stock_new2'
res = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
soup = BeautifulSoup(res.text, 'html.parser')
data = soup.find_all('td', {'class':'gall_num'})
gall_num = list()

for i in data:
    tmp = i.get_text()
    if tmp.isdigit():
        gall_num.append(int(tmp))

data = list()

for i in range(0, len(gall_num)):
    try:
        url = f'https://gall.dcinside.com/board/view/?id=stock_new2&no=7701820https://gall.dcinside.com/board/view/?id=stock_new2&no={gall_num[i]}'
        res = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
        soup = BeautifulSoup(res.text, 'html.parser')

        title = soup.select_one("#container > section > article:nth-child(3) > div.view_content_wrap > header > div > h3 > span.title_subject").get_text()
        user = soup.select_one("#container > section > article:nth-child(3) > div.view_content_wrap > header > div > div > div.fl")

        nickname = user.find('em').get_text()
        user_ip = user.find('span', {'class':'ip'}).get_text()
        time = user.find('span', {'class':'gall_date'}).get_text()
        description = soup.select_one('#container > section > article:nth-child(3) > div.view_content_wrap > div > div.inner.clear > div.writing_view_box').get_text()
        description = description.replace('\n','')

        data.append([gall_num[i], nickname, user_ip, time, title, description])

    except:
        continue

df = pd.DataFrame(data, index=None)
df.columns = ['번호','닉네임','아이피','시간','제목','본문']

df.to_csv('dcinside.csv', encoding="utf-8-sig")