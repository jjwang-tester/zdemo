from django.conf.urls import url
from brequest import views
urlpatterns = [
    url(r'^login/$', views.login),
]