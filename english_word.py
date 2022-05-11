from bs4 import BeautifulSoup
import requests

subjects = list()

res = requests.get('https://basicenglishspeaking.com/daily-english-conversation-topics/')

soup = BeautifulSoup(res.text, 'html.parser')

divs = soup.find_all('div', {'class':'tcb-flex-row tcb--cols--3'})

print(divs)
 
for link in divs[0].find_all('a'):
    subject = link.text
    subjects.append(subject)

print(subjects)
