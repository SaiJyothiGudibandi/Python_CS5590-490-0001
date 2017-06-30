import requests                         #gettig the URL
from bs4 import BeautifulSoup
import os

url = "https://www.python.org/about/gettingstarted/"
source_code = requests.get(url)
plain_text = source_code.content
soup = BeautifulSoup(plain_text, "html.parser")
result_list = soup.findAll('div')
#print(result_list)
for div in result_list:
    R1=div.find('h1')
    print("h1:",R1)


source_code = requests.get(url)
plain_text = source_code.content
soup = BeautifulSoup(plain_text, "html.parser")
body = soup.findAll('body')
divs = soup.findAll('div')
for h1 in divs:
    h=h1.findAll('h1')
    print("h1 in body:",h)

