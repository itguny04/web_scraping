import requests
from bs4 import BeautifulSoup

url = 'https://gall.dcinside.com/board/lists/?id=stock_new2'
res = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
soup = BeautifulSoup(res.text, 'html.parser')
data = soup.find_all('td', {'class':'gall_num'})[4:]
gall_num = list(map(lambda x:int(x.get_text()), data))

url = 'https://gall.dcinside.com/board/view/?id=stock_new2&no=7701820https://gall.dcinside.com/board/view/?id=stock_new2&no=7701820'
res = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
soup = BeautifulSoup(res.text, 'html.parser')

title = soup.select_one("#container > section > article:nth-child(3) > div.view_content_wrap > header > div > h3 > span.title_subject").get_text()
user = soup.select_one("#container > section > article:nth-child(3) > div.view_content_wrap > header > div > div > div.fl")

nickname = user.find('em').get_text()
user_ip = user.find('span', {'class':'ip'}).get_text()

print(user_ip)


description = soup.select_one('#container > section > article:nth-child(3) > div.view_content_wrap > div > div.inner.clear > div.writing_view_box').get_text()
description = description.replace('\n','')
