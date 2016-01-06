# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160105_0102'),
    ]

    operations = [
        migrations.AddField(
            model_name='account_notes',
            name='pay_type',
            field=models.CharField(max_length=3, choices=[('1', '现金'), ('2', '信用卡'), ('3', '支付宝'), ('4', '实体消费券'), ('5', '电子消费券')]),
        ),
    ]
