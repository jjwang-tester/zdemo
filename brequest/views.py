from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse
import json
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

# 4.非form表单解析：json xml str
def login_not_form(request):

    # 解析 非form表单的参数 request.body 返回的对象是 二进制 bytes
    b_data = request.body
    str_data = b_data.decode()
    json_data = json.loads(str_data)
    print(b_data)
    print(type(b_data))
    print(str_data)
    print(type(str_data))

    # 如果参数是json的 bytes--str--dict
    print(json_data)
    print(type(json_data))

    return HttpResponse('4.非form表单参数解析：json xml str')

# 5.请求头信息
def login_headers(request):
    # request.META meta
    headers = request.META
    print(headers)
    print(type(headers))

    # 交互的格式
    print(headers['CONTENT_TYPE'])

    return HttpResponse('5.请求头信息')