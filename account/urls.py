from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.login, name='auth_views.login'),
    url(r'^simple_login/$', views.simple_login, name='simple_login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^change_password/$', views.change_password, name='change_password'),

]