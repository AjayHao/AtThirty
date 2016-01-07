from django.conf.urls import patterns, url

from app.note import views as note_views


urlpatterns = [
    #django url
    url(r'^$', note_views.notes, name='notes'),   
    url(r'^get_notes/$',note_views.get_notes),
    url(r'^get_securities/$',note_views.get_securities),
    url(r'^get_accounts/$',note_views.get_accounts), 
    url(r'^change_note/$',note_views.change_note),  
    url(r'^delete_note/(?P<noteid>\d+)/$',note_views.delete_note),         
]
