# -*- coding: utf-8 -*-
import json

from django.core import serializers
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import ensure_csrf_cookie

from app.note.models import *


# Create your views here.
@ensure_csrf_cookie

def notes(req):
    return render_to_response('notes.html')

def note(req, noteid=None):
    if req.method == 'POST':
        ret = change_note(req)
    elif req.method == 'DELETE':
        ret = delete_note(req, noteid)
                
    return HttpResponse(json.dumps(ret), content_type="application/json")  

def get_securities(req):
    qNoteId = req.GET['note_id']
    securities = Invest_Notes.objects.filter(note_id=qNoteId)
    #temp = json.loads(serializers.serialize("json", securities))
    ret =  []
    for item in securities:
        f = {}
        #f = item['fields']
        f['secu_name'] = item.security_name
        f['direction'] = dict(label=item.get_direction_display(), value=item.direction)
        f['unit_price'] = float(item.unit_price)
        f['quantity'] = float(item.quantity)
        f['total_price'] = float(item.total_price)
        ret.append(f)
    return HttpResponse(json.dumps(ret), content_type="application/json")

def get_accounts(req):
    qNoteId = req.GET['note_id']
    accounts = Account_Notes.objects.filter(note_id=qNoteId)
    #temp = json.loads(serializers.serialize("json", securities))
    ret =  []
    for item in accounts:
        f = {}
        #f = item['fields']
        f['commodity_name'] = item.commodity_name
        f['commodity_type'] = dict(label=item.get_commodity_type_display(), value=item.commodity_type)
        f['pay_type'] = dict(label=item.get_pay_type_display(), value=item.pay_type)
        f['direction'] = dict(label=item.get_direction_display(), value=item.direction)
        f['total_price'] = float(item.total_price)
        ret.append(f)
    return HttpResponse(json.dumps(ret), content_type="application/json")

def get_notes(req):
    qBegin = req.GET['start']
    qEnd = req.GET['end'] 
    qNoteType = req.GET.getlist('note_type[]')
    
    evnts = Notes.objects.exclude(
                Q(begin_date__gte=qEnd) | Q(end_date__lte=qBegin)
            ).filter(
                note_type__in=qNoteType
            )  
        
    #print(evnts)
    #ret = evnts.values()
    ''' I 've to find a better way here to solve choice problems in CharField,
    now I just bet that python solves more efficiently then what js does..
    '''
    ret = []   
    #for i in range(len(evnts)):
    for e in evnts:
        d = {}
        d['note_id'] = e.id
        #for fullcalendar display ..begin
        d['title'] = e.title      
        d['start'] = e.begin_date 
        d['end'] = e.end_date
        if e.is_all_day == '1':
            d['allDay'] = True
        else:
            d['allDay'] = False
        #for fullcalendar display ..end
        d['note_title'] = e.title      
        d['begin_date'] = e.begin_date 
        d['end_date'] = e.end_date        
        d['is_all_day'] = e.is_all_day
        d['note_type'] = e.note_type
        d['note_type_name'] = e.get_note_type_display()
        d['remark'] = e.remark
         
        ret.append(d)
    #print(ret)   
    return HttpResponse(json.dumps(ret), content_type="application/json")

def change_note(req):

    ret = {'retCode':'0', 'retMsg':'修改成功'}
    try:
        req_json = json.loads(req.body.decode())
        note_id = req_json['note_id']
        note_type = req_json['note_type']
        note_title = req_json['note_title']
        remark = req_json['remark'] 
        begin_date = req_json['begin_date'] 
        end_date = req_json['end_date'] 
        is_all_day = req_json['is_all_day']

        #print(note_id)
        if note_id == '' :
            #create new notes
            note = Notes.objects.create(begin_date=begin_date,
                                        end_date=end_date,
                                        note_type=note_type,
                                        title=note_title,
                                        remark=remark,
                                        is_all_day=is_all_day
                                        )
        else:
            if note_type == '2' :
            #remove old securities
                for i in Invest_Notes.objects.filter(note_id=note_id):
                    i.delete()
            #remove old accounts
            elif note_type == '3' :
                for a in Account_Notes.objects.filter(note_id=note_id):
                    a.delete()
            
            #save to origin notes
            note = Notes.objects.get(id=note_id)
            note.begin_date = begin_date
            note.end_date = end_date
            note.is_all_day = is_all_day
            note.title = note_title
            note.remark = remark
            note.save()

        if note_type == '2' :
            securities = req_json['securities']
            for s in securities:
                d_obj = s['direction']
                #create new securities
                Invest_Notes.objects.create(security_name= s['secu_name'],
                                            direction= d_obj['value'],
                                            unit_price= s['unit_price'],
                                            quantity= s['quantity'],
                                            total_price= s['total_price'],
                                            note = note
                                            )
                
        elif note_type == '3' :
            accounts = req_json['accounts']
            for a in accounts:
                ct_obj = a['commodity_type']
                d_obj = a['direction']
                p_obj = a['pay_type']
                #create new securities
                Account_Notes.objects.create(commodity_name= a['commodity_name'],
                                            commodity_type= ct_obj['value'],
                                            direction= d_obj['value'],
                                            pay_type= p_obj['value'],
                                            total_price= a['total_price'],
                                            note = note
                                            )                
    except Exception as e:
        print(e)
        ret['retMsg'] = e            
    return ret

def delete_note(req, noteid=None):
    ret = {'retCode':'0', 'retMsg':'删除成功'}
    try:
        note = Notes.objects.get(id=noteid)
        note.delete()
    except Exception as e:
        print(e)
        ret['retMsg'] = e            
    return ret  
          