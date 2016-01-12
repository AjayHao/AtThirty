from django.conf.urls import patterns, url

from app.note import views as note_views


urlpatterns = [
    #django url with RESTful style
    url(r'^$', note_views.notes),   
    url(r'^get_notes/$', note_views.get_notes),
    url(r'^get_securities/$', note_views.get_securities),
    url(r'^get_accounts/$', note_views.get_accounts),  
    url(r'^note/$', note_views.note),       
    url(r'^note/(?P<noteid>\d+)/$', note_views.note),    
]
