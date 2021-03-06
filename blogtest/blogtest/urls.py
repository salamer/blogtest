"""blogtest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','article.views.home', name='home'),
    url(r'^write/','article.views.write',name='write'),
    url(r'^login/','article.views.login',name='login'),
    url(r'^post/(?P<id>\d+)/$','article.views.post',name='post'),
    url(r'^logined/','article.views.logined',name='logined'),
    url(r'^posted/','article.views.posted',name='posted'),
    url(r'^commented/','article.views.commented',name='posted'),
    url(r'^register/','article.views.register',name='register'),
    url(r'^registered/','article.views.registered',name='registered'),
    url(r'^logout/','article.views.logout',name='logout'),
    url(r'^category/(?P<category>\w+)/$','article.views.category_search',name='category'),
    url(r'^usershow/(?P<username>\w+)/$','article.views.usershow',name='usershow'),
    url(r'^formcheck/$','article.views.formcheck', name='formcheck'),
]
