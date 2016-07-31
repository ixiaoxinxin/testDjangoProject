from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$','lists.views.home_page',name='home'),
    url(r'^lists/', include('lists.urls')),
    url(r'^admin/', include(django.contrib.admin.urls)),

]
