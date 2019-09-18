#!/usr/bin/python
#*-----encoding=utf8-----*

from bs4 import BeautifulSoup
from lxml import html
import xml
import requests

url =  "https://movie.douban.com/chart"
f = requests.get(url)
soup = BeautifulSoup(f.content,'lxml')

# print(soup)
# print(f.content.decode())
content = soup.find_all('div',class_="pl2")
# print(content)

for k in content:
    a = k.find_all('span')
    print(a[0].string)

print('========================')
print('this is end')
print('========================')
