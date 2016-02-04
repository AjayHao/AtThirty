from django.conf.urls import patterns, url

from app.blog import views as blog_views


urlpatterns = [
    #django url
    url(r'^$', blog_views.index, name='blog_index'),
    
]
