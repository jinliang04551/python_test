#-*-coding:utf-8-*-
#!/usr/local/bin/python3.7

import requests
import csv
import random
import time
import socket
import http.client
import lxml
# import urllib.request
from bs4 import BeautifulSoup


def get_content(url,data=None):
    header={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
    }
    
    timeout = random.choice(range(80,180))
    while True:
        try:
            rep = requests.get(url,timeout=timeout)
            rep.encoding = 'utf-8'
            break
        except socket.timeout as e:
            print('3:',e)
            time.sleep(random.choice(8,15))

        except socket.error as e:
            print('4:',e)
            time.sleep(random.choice(20,60))
        except http.client.IncompleteRead as e:
            print('5:',e)
            time.sleep(random.choice(5,15))
        print(rep.text)

    return rep.text

def get_data(html_text):
    final = []
    bs = BeautifulSoup(html_text,"lxml")
    #获取body
    body = bs.body 
    #找到id为7d的div
    data = body.find('div',{'id':'main'})

    col2 = data.find(attrs={'class':'col2'})
    
    box =  data.find(attrs={'class':'box'})

    #获取ul部分
    ul = data.find('ul')
    #获取所有的li
    li = ul.find_all('li')
    
    #对每个li标签中的内容进行遍历
    for s in li:
        temp = []
        print(s)
        a = s.find_all('a')
        print('a',a)
       

        # span = a.find_all('span')
        # print('span',span)

        for k in a:
            href = k['href']
            target = k['target']
            font = k.find(attrs={'font':'col2'})
            text = k.get_text()

            print('%%%%%%%%%%%%%%%%%%%%%%%%%%')
            print('herf:',href)
            print('target:',target)
            print('string:',k.string)
            print('text:',text)

            print('%%%%%%%%%%%%%%%%%%%%%%%%%%')
            temp.append(text)

        # color = s.select('li[font color="#FF0000"]')
        # print('\ncolor:',color)
        final.append(temp)
    return final  

def write_data(data,name):
    file_name = name
    with open(file_name,'a',errors='ignore',newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(data)

if __name__ == '__main__':
    url = 'http://www.hao6v.com'
    html = get_content(url)
    # print('=================================')
    # print('html',html)
    # print('=================================')
    result = get_data(html)
    print('=================================')
    print('result',result)
    print('=================================')

    write_data(result,'movies.csv')
    
