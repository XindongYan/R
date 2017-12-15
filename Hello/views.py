from django.shortcuts import render
from django.http import HttpResponse, response
from .address import get_data
from bs4 import BeautifulSoup
import json


def index(request):
    return render(request, 'index.html')


def test(request):
    with open('C:/Users/Yenda/Desktop/所有文件/Bottle-Web- Project/rent.csv', 'r') as f:

        f = f.read()
        f = [f]
        print(f)

        return render(request, 'test.html', { 'address': f })


def map(request):
    if request.method == 'POST':
        text = request.POST['text']

        res = render(request, 'post.html', {'text': text})
        # res.set_cookie('position', text)

        return res
    else:
        return HttpResponse(u'Hello Re')

html = 'http://hf.58.com/zufang/'


def serch(request):
    if request.method == "POST":
        #调用address中的main函数
        HTML = get_data(html)
        HTML = str(HTML)

        '''bs4解析'''
        HTML = BeautifulSoup(HTML, 'html.parser')
        soup = HTML.find_all('p', class_="add")

        list = []

        '''输出地址'''
        for i in soup:
            text = ''.join(i.get_text().split())
            print([text])
            list += [text]

        '''打印输出'''
        print(list)

        text = request.POST['text']
        res = render(request, 'test2.html', {'address': list})

        '''发送房源地址'''
        return res
    else:
        return HttpResponse(u'发生错误')


def route(request):
    if request.method == 'POST':
        # new_map = map(request)
        # print(new_map)
        parameter = request.POST['route']

        return render(request, 'beta.html', {'position': parameter})


# Create your views here.
