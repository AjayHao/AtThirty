# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response

# Create your views here.
# @ensure_csrf_cookie
def index(req):
    return render_to_response('index.html',{"blog_subtitle":"控制台"})

def reports(req):
    return render_to_response('reports.html',{"blog_subtitle":"报表"})

def guides(req):
    return render_to_response('guidely.html')

def charts(req):
    return render_to_response('charts.html')

def shortcodes(req):
    return render_to_response('shortcodes.html')