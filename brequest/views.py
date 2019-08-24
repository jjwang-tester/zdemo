from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse

# 1.解析拼接参数！
def login_connect(request, city, year):
    print('解析拼接路径的参数---年份', year)
    print('解析拼接路径的参数---城市', city)
    return HttpResponse("1.解析拼接参数！")

# 2.解析查询参数！
def login_query(request):
    # 解析查询参数 request.GET 熟悉
    params = request.GET
    print(params)
    print(type(params))
    print(params.getlist('a'))
    print(params.getlist('a')[0])
    print(params.get('b'))

    return HttpResponse("2.解析查询参数！")

# 3.form表单参数的解析
def login_form(request):
    params = request.POST
    print(params)
    print(type(params))
    print(params.getlist('a'))
    print(params.getlist('a')[0])
    print(params.get('b'))

    return HttpResponse('3.form表单参数的解析')