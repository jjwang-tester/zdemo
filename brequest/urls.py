from django.conf.urls import url
from brequest import views
urlpatterns = [

    # 1.拼接路径  2008/beijing/
    url(r'^login/(?P<year>\d{4})/(?P<city>[a-zA-Z]+)/$', views.login_connect),

]