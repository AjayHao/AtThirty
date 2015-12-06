# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from app.sysAdmin.models import Sche
import json
# Create your views here.
# @ensure_csrf_cookie
def index(req):
    return render_to_response('blog_index.html')

def reports(req):
    return render_to_response('reports.html',{"blog_subtitle":"报表"})

def guides(req):
    return render_to_response('guidely.html')

def charts(req):
    return render_to_response('charts.html')

def shortcodes(req):
    return render_to_response('shortcodes.html')

def schedules(req):
    return render_to_response('schedules.html',{"blog_subtitle":"日程"})

def get_sche_events(req):
    ret = []
    evnts = Sche.objects.all()
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