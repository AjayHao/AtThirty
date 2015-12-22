from django.conf.urls import patterns, url

from app.blog import views as blog_views


urlpatterns = [
    #django url
    url(r'^$', blog_views.index, name='blog_index'),
    url(r'^notes$', blog_views.notes, name='notes'),   
    url(r'^get_notes/$',blog_views.get_notes),
    url(r'^change_note/$',blog_views.change_note),     
]
