# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account_notes',
            name='commodity_type',
            field=models.CharField(max_length=3, choices=[('1', '日用品'), ('2', '餐饮'), ('3', '水电煤'), ('4', '人情')]),
        ),
        migrations.AlterField(
            model_name='account_notes',
            name='direction',
            field=models.CharField(max_length=1, choices=[('1', '收入'), ('2', '支出')]),
        ),
        migrations.AlterField(
            model_name='invest_notes',
            name='direction',
            field=models.CharField(max_length=1, choices=[('1', '买入'), ('2', '卖出')]),
        ),
    ]
