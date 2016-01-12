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
    INVEST_DIRECTIONS = (
        ('1', '买入'),
        ('2', '卖出'),
    )    
    
    note = models.ForeignKey(Notes)
    security_name = models.CharField(max_length=50)
    direction = models.CharField(max_length=1, choices=INVEST_DIRECTIONS)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2,default=0)
    quantity = models.DecimalField(max_digits=12, decimal_places=4,default=0)
    total_price = models.DecimalField(max_digits=12, decimal_places=2,default=0)
    
    def __str__(self):
        return self.notes

    class Meta:
        db_table = 'notes_investments'        
    
class Account_Notes(BaseModel):    
    COMMODITY_TYPES = (
        ('1', '日用品'),
        ('2', '餐饮'),
        ('3', '水电煤'),
        ('4', '人情'),
        ('5', '其他'),
    )    
    
    MONEY_DIRECTIONS = (
        ('1', '收入'),
        ('2', '支出'),
    )    
    
    PAY_TYPES = (
        ('1', '现金'),
        ('2', '信用卡'),
        ('3', '支付宝'),
        ('4', '实体消费券'),
        ('5', '电子消费券'),
    )
    
    note = models.ForeignKey(Notes)
    commodity_name = models.CharField(max_length=50)
    commodity_type =  models.CharField(max_length=3,choices=COMMODITY_TYPES,blank=True,null=True)
    pay_type = models.CharField(max_length=3,choices=PAY_TYPES)
    direction = models.CharField(max_length=1,choices=MONEY_DIRECTIONS)
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    
    def __str__(self):
        return self.notes

    class Meta:
        db_table = 'notes_accounts'      