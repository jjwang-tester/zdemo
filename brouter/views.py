from django.shortcuts import render
from django.http.response import HttpResponse
from django.urls.base import reverse


# Create your views here.

def login(request):

    # 路由反解析 -- 根据 视图函数 request 反向推理当前的路由是什么？
    print("有namespace反向解析---：", reverse('brouter:login'))
    return HttpResponse("研究的功能，现在是路由的屏蔽和加载顺序")

def register(request):

    #

    return HttpResponse("注册功能！")