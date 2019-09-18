#-*-coding:utf-8-*-
#!/usr/local/bin/python3.7

import requests
import csv
import random
import time
import socket
import http.client
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
    bs = BeautifulSoup(html_text,"html.parser")
    #获取body
    body = bs.body 
    #找到id为7d的div
    data = body.find('div',{'id':'7d'})
    #获取ul部分
    ul = data.find('ul')
    #获取所有的li
    li = ul.find_all('li')

    #对每个li标签中的内容进行遍历
    for day in li:
        temp = []
        #找到日期
        date = day.find('h1').string
        #添加到temp中
        temp.append(date)
        #找到里中的所有p标签
        inf = day.find_all('p')
        #第一个p标签中的内容（天气状况）加到temp中
        if inf[1].find('span') is None:
            # 天气预报可能没有当天的最高气温（到了傍晚，就是这样），需要加个判断语句,来输出最低气温
            temperature_highest = None
        else:
             # 找到最高温
            temperature_highest = inf[1].find('span').string
            temperature_highest = temperature_highest.replace('℃','')

            # 找到最低温
            temperature_lowest = inf[1].find('i').string
            temperature_lowest = temperature_lowest.replace('℃','')

            temp.append(temperature_highest)
            temp.append(temperature_lowest)
            final.append(temp)
    return final  

def write_data(data,name):
    file_name = name
    with open(file_name,'a',errors='ignore',newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(data)

if __name__ == '__main__':
    url = 'http://www.weather.com.cn/weather/101190401.shtml'
    html = get_content(url)
    print('=================================')
    print('html',html)
    print('=================================')
    result = get_data(html)
    print('=================================')
    print('result',result)
    print('=================================')

    file_name = 'weather.csv'
    write_data(result,'weather.csv')
    
