import requests
from bs4 import BeautifulSoup as bs

url = "https://jupiter.challenges.picoctf.org/problem/56830/"
robots_url = url+"1bb4c.html"
response = requests.get(robots_url)
soup = bs(response.text, 'html.parser')
flag = soup.find('flag').text
print(flag)