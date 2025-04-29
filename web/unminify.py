import requests as r 
from bs4 import BeautifulSoup as bs
url = "http://titan.picoctf.net:61234/"

response = r.get(url)
soup = bs(response.text, 'html.parser')
flag = soup.find_all('p')[1].get("class")
print(flag[0])

