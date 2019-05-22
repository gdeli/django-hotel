from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'hotel'

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^review/(?P<pk>\d+)/$', views.review, name="review"),    
]