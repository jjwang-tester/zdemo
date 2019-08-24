from django.conf.urls import url

from cresponse import views
urlpatterns = [

    # 普通响应
    url(r'^response/$', views.login_response),

    # json数据响应
    url(r'^response_json/$', views.login_JsonResponse),

    # 重定向redirect
    url(r'^response_redirect/$', views.login_redirect)
]