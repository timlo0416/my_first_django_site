"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from . import views
from django.contrib.auth.views import login, logout
urlpatterns = [
    url(r'^accounts/logout/$', views.logout, name='logout'),
    #url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^$', views.post_list, name='post_list'),
    url(r'^index/$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/edit/(?P<pk>[0-9]+)/$', views.post_edit, name='post_edit'),
    url(r'^accounts/profile', views.post_new, name='profile'),
]
