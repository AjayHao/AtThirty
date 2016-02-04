from django.conf.urls import patterns, url

from app.lab import views as lab_views


urlpatterns = [
    #django url
    url(r'^markdown_ref/$', lab_views.markdown_ref),
]
