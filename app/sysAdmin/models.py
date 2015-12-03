# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Sche(models.Model):
    title = models.CharField(max_length=8)
    begindate = models.CharField(max_length=20)
    enddate = models.CharField(max_length=20)
    allday = models.CharField(max_length=1)
    userid = models.CharField(max_length=30)
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'sche_test'