# -*- coding: utf-8 -*-
from django.conf.urls import include, url
import views as list_views
import urls as list_urls

urlpatterns = [
    url(r'^$', list_views.home_page, name='home'),
    url(r'^lists/', include(list_urls)),
    url(r'^admin/', include('django.contrib.admin')),
]

