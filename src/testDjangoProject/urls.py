from django.conf.urls import include, url


urlpatterns = [
    url(r'^$','lists.views.home_page',name='home'),
    url(r'^lists/', include('lists.urls')),
    url(r'^admin/', include(admin.site.urls)),

]
