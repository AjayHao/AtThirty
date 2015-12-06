"""AtThirty URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
import os

urlpatterns = [
####this line don't delete!!!
#url(r'^admin/', include(admin.site.urls)),
    
#    url(r'^$', adminViews.index, name='index'),   
    url(r'^', include('app.blog.urls')),    
    url(r'^blog_admin/', include('app.sysAdmin.urls')),    
    #url(r'^dashboard/', adminViews.index, name='index'),         
    #url(r'^reports/', adminViews.reports, name='reports'),
    #url(r'^guides/', adminViews.guides, name='guides'),
    #url(r'^charts/', adminViews.charts, name='charts'),
    #url(r'^shortcodes/', adminViews.shortcodes, name='shortcodes'), 
    #url(r'^schedules/', adminViews.schedules, name='schedules'),
    #url(r'^get_sche_events/$',adminViews.get_sche_events),
    
    #url(r'^css/(?P<path>.*)$' , 'django.views.static.serve', 
    #     {'document_root': settings.GLOBAL_CSS_DIR} ) ,
    #url(r'^js/(?P<path>.*)$' , 'django.views.static.serve', 
    #     {'document_root':  settings.GLOBAL_JS_DIR} ) ,
    #url(r'^img/(?P<path>.*)$' , 'django.views.static.serve', 
    #     {'document_root':  settings.GLOBAL_IMG_DIR} ) ,
    #url(r'^font/(?P<path>.*)$' , 'django.views.static.serve', 
    #     {'document_root':  settings.GLOBAL_FONT_DIR} ) ,
               
]
