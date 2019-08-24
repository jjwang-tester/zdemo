from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse

def login_connect(request,city,year):
    print('解析拼接路径的参数---年份',year)
    print('解析拼接路径的参数---城市',city)
    return HttpResponse("1 、request请求对象的传参！")