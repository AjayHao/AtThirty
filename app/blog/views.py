# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.db.models import Q
from app.blog.models import *
import json
from _mysql import NULL
# Create your views here.
# @ensure_csrf_cookie
def index(req):
    return render_to_response('blog_index.html')

def notes(req):
    return render_to_response('notes.html')

def get_notes(req):
    
    qBegin = req.GET['start']
    qEnd = req.GET['end'] 
    qNoteType = req.GET.getlist('note_type[]')
    
    evnts = Notes.objects.exclude(
                Q(begin_date__gte=qEnd) | Q(end_date__lt=qBegin)
            )
    
    if  len(qNoteType) > 0 :
        evnts = evnts.filter(
            note_type__in=qNoteType
        )  
        
    #print(evnts)
    #ret = evnts.values()
    ''' I 've to find a better way here to solve choice problems in CharField,
    now I just bet that python solves more efficiently then what js does..
    '''
    ret = []   
    for e in evnts:
        d = {}
        d['note_id'] = e.id
        d['title'] = e.title
        d['start'] = e.begin_date
        d['end'] = e.end_date
        d['note_type'] = e.note_type
        d['note_type_name'] = e.get_note_type_display()
        d['remark'] = e.remark
        #print(d)
        if e.is_all_day == '1':
            d['addDay'] = True
        else:
            d['addDay'] = False
            
        '''
        pure front-end process will be executed in the front
        if e.note_type == '1':
            d['className'] = 'memo_color'
        elif e.note_type == '2':
            d['className'] = 'invest_color'
        elif e.note_type == '3':
            d['className'] = 'account_color'    
        '''
        ret.append(d)

    print(ret)    
    return HttpResponse(json.dumps(ret), content_type="application/json")