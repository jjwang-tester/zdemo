from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse

def login(request):

    return HttpResponse("1 、request请求对象的传参！")