# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from app.blog.models import *
import json
# Create your views here.
# @ensure_csrf_cookie
def index(req):
    return render_to_response('blog_index.html')

def schedules(req):
    return render_to_response('schedules.html')

def get_sche_events(req):
    ret = []
    qbegin = req.GET['start']
    qend = req.GET['end'] 
    evnts = Sche.objects.filter(begindate__range=(qbegin,qend))

    for e in evnts:
        d = {}
        d['title'] = e.title
        d['start'] = e.begindate
        d['end'] = e.enddate
        if e.allday == '1':
            d['addDay'] = True
        else:
            d['addDay'] = False
        ret.append(d)
   
    return HttpResponse(json.dumps(ret), content_type="application/json")