import requests
from bs4 import BeautifulSoup as bs
url = "https://jupiter.challenges.picoctf.org/problem/17682/"

response = requests.get(url)   
print(response.text) 
