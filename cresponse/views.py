from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.http.response import JsonResponse

# 普通响应对象
def login_response(request):
    # 1. 操作 参数
    # return HttpResponse(
    #     content="浏览器显示的内容",
    #     # 服务器接收内容的类型
    #     # content_type='application/json',
    #     # status=200,
    # )

    # 2. 操作 属性
    # 实例一个response对象
    response = HttpResponse()
    # 设置属性
    response.content = '操作属性'
    response.status_code = 200
    response.status_code = HttpResponseBadRequest.status_code
    # 返回实例化对象（被请求的响应）

    return response


# 操作 JsonResponse
# 帮我们做了两件事
# 1.content_type = 'application/json'
# 2.json_dict 转换成了 json_str
def login_JsonResponse(request):
    dict_data = {
        'a': 1,
        'b': 2,
    }

    return JsonResponse(dict_data)
