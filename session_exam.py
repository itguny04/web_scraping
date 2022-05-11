from bs4 import BeautifulSoup
import requests

MEMBER_DATA = {
    'memberID':'kgh2133',
    'memberPassword':'qw1234567890!'
}

with requests.Session() as s:
    res = s.post('http://dowellcomputer.com/member/memberLoginAction.jsp', data=MEMBER_DATA)
    res = s.get('http://dowellcomputer.com/member/memberUpdateForm.jsp?ID=kgh2133')

    soup = BeautifulSoup(res.text, 'html.parser')

    result = soup.findAll('input')
    print(result[1].get('value'), result[2].get('value'), sep="\n")

