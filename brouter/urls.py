
from django.conf.urls import url
from brouter import views


urlpatterns = [
    url(r'^login/$', views.login)
]