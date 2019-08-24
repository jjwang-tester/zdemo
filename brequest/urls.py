from django.conf.urls import url
from brequest import views
urlpatterns = [

    # 1.拼接参数  2008/beijing/
    url(r'^brequest_connect/(?P<year>\d{4})/(?P<city>[a-zA-Z]+)/$', views.login_connect),

    # 2.解析查询参数 ？a=10&b=20 解析查询参数
    url(r'^brequest_query/$', views.login_query)
]