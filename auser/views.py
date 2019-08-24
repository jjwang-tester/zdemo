from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
'''
# 创建视图函数 
    1. 接收请求对象
    2. 解析请求对象
    3. model,template
    4. 返回响应对象
'''
def index(request):

    # 返回响应对象 快速导包快捷键（alt + enter）
    return HttpResponse('hello world 第一次使用Django写项目！')