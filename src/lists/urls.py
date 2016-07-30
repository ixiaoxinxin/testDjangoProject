# -*- coding: utf-8 -*-
from django.conf.urls import include,url, patterns


urlpatterns = patterns['',
    url(r'^(\d+)$','lists.views.viewlist', name='viewlist'),
    url(r'^(\d+)/add_item$','lists.views.add_item', name='add_item'),
    url(r'^new$','lists.views.new_list',name='new_list'),

]
