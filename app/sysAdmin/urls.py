from django.conf.urls import patterns, url

from app.sysAdmin import views


urlpatterns = [
    #django url
    url(r'^$', views.index, name='admin_index'),
]
