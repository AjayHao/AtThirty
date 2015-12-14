# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response

# Create your views here.
# @ensure_csrf_cookie
def index(req):
    return render_to_response('admin_index.html',{"blog_subtitle":"控制台"})

def button(req):
    return render_to_response('buttons.html',{"blog_subtitle":"控制台"})