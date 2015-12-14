# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
        
        
class Notes(BaseModel):
    
    NOTE_TYPES = (
        ('1', '备忘录'),
        ('2', '投资'),
        ('3', '记账'),
    )
    
    title = models.CharField(max_length=50)
    note_type = models.CharField(max_length=2, choices=NOTE_TYPES)
    begin_date = models.CharField(max_length=20)
    end_date = models.CharField(max_length=20)
    is_all_day = models.CharField(max_length=1)
    user_id = models.CharField(max_length=30,default="ajay")
    remark = models.TextField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'notes'  
         
        
class Invest_Notes(BaseModel): 
    note = models.ForeignKey(Notes)
    security_name = models.CharField(max_length=50)
    buy_unit_price = models.DecimalField(max_digits=6, decimal_places=2,default=0)
    quantity = models.DecimalField(max_digits=12, decimal_places=4,default=0)
    total_price = models.DecimalField(max_digits=12, decimal_places=2,default=0)
    
    def __str__(self):
        return self.notes

    class Meta:
        db_table = 'notes_investments'        
    
class Account_Notes(BaseModel):    
    note = models.ForeignKey(Notes)
    commodity_name = models.CharField(max_length=50)
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    
    def __str__(self):
        return self.notes

    class Meta:
        db_table = 'notes_accounts'      