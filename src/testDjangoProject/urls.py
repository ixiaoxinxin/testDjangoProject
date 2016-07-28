# -*- coding: utf-8 -*-
"""testDjangoProject URL Configuration

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
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin


urlpatterns = patterns['',
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', 'lists.views.home_page', name='home')
    url(r'^$','lists.views.home_page',name='home'),
    url(r'^lists/the-only-list-in-the-world/$','lists.views.viewlists',name='viewlists'),#这种写法只支持1.1版本，1.9版本不支持
    #url(r'^s', view),
    #添加 url 映射用于重定向
    url(r'^lists/new$','lists.views.new_lists',name='new_lists'),

]
