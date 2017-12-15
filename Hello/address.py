from bs4 import BeautifulSoup
from django.shortcuts import render
from urllib import request

html = 'http://hf.58.com/zufang/'

def get_data(html):
    # 获取网页代码
    data = request.urlopen(html)
    data = data.read()

    # bs4解析
    soup = BeautifulSoup(data, 'html.parser')
    doc = soup.find_all('li', _class="")

    #返回值到get_data()
    return doc