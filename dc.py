from email import header
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

gall_num = list()
datas = list()

blackword = ['시발', '게이', '급식', '꼰대' ,'ㅅㅂ', '새끼', '섹스', 'ㅂㅅ' ,'씨발', '병신', '좆', '십새', '정액']
blacklist = list()

for i in range(1,5):
    url = f'https://gall.dcinside.com/board/lists?id=ib_new2&page={i}'
    res = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
    soup = BeautifulSoup(res.text, 'html.parser')
    data = soup.find_all('td', {'class':'gall_num'})
    
    for j in data:
        tmp = j.get_text()
        if tmp.isdigit():
            gall_num.append(int(tmp))


for i in range(0, len(gall_num)):
    try:
        url = f'https://gall.dcinside.com/board/view/?id=ib_new2&no={gall_num[i]}'
        res = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
        soup = BeautifulSoup(res.text, 'html.parser')

        title = soup.select_one("#container > section > article:nth-child(3) > div.view_content_wrap > header > div > h3 > span.title_subject").get_text()
        user = soup.select_one("#container > section > article:nth-child(3) > div.view_content_wrap > header > div > div > div.fl")

        nickname = user.find('em').get_text()
        user_ip = user.find('span', {'class':'ip'}).get_text()
        time = user.find('span', {'class':'gall_date'}).get_text()
        description = soup.select_one('#container > section > article:nth-child(3) > div.view_content_wrap > div > div.inner.clear > div.writing_view_box').get_text()
        description = description.replace('\n','')
        description = re.sub('/(?:(?:https?|ftp|file):\/\/|www\.|ftp\.)(?:\([-A-Z0-9+&@#\/%=~_|$?!:,.]*\)|[-A-Z0-9+&@#\/%=~_|$?!:,.])*(?:\([-A-Z0-9+&@#\/%=~_|$?!:,.]*\)|[A-Z0-9+&@#\/%=~_|$])/igm', '', description)

        datas.append([gall_num[i], nickname, user_ip, time, title, description])

    except:
        continue

for data in datas:
    black = False
    for _ in blackword:
        if data[5].find(_) != -1 or data[4].find(_) != -1:
            rp_text = '*'*len(_)
            data[5] = data[5].replace(_, rp_text)
            data[4] = data[4].replace(_, rp_text)
            black = True
    
    if black:
        blacklist.append(data)


df = pd.DataFrame(blacklist, index=None)
df.columns = ['번호','닉네임','아이피','시간','제목','본문']
df.to_csv('dcinside.csv', encoding="utf-8-sig")