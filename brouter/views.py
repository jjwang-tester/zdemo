from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.

def login(request):
    return HttpResponse("研究的功能，现在是路由的屏蔽和加载顺序")
