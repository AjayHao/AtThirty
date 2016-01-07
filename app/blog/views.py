# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response


# Create your views here.
# #@#ensure_csrf_cookie
def index(req):
    return render_to_response('blog_index.html')

def lab_angularjs(req):
    return render_to_response('lab_angularjs.html')