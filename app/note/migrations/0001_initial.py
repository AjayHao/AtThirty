# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account_Notes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('modify_time', models.DateTimeField(auto_now=True)),
                ('commodity_name', models.CharField(max_length=50)),
                ('commodity_type', models.CharField(choices=[('1', '日用品'), ('2', '餐饮'), ('3', '水电煤'), ('4', '人情')], max_length=3, blank=True, null=True)),
                ('pay_type', models.CharField(choices=[('1', '现金'), ('2', '信用卡'), ('3', '支付宝'), ('4', '实体消费券'), ('5', '电子消费券')], max_length=3)),
                ('direction', models.CharField(choices=[('1', '收入'), ('2', '支出')], max_length=1)),
                ('total_price', models.DecimalField(max_digits=12, decimal_places=2)),
            ],
            options={
                'db_table': 'notes_accounts',
            },
        ),
        migrations.CreateModel(
            name='Invest_Notes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('modify_time', models.DateTimeField(auto_now=True)),
                ('security_name', models.CharField(max_length=50)),
                ('direction', models.CharField(choices=[('1', '买入'), ('2', '卖出')], max_length=1)),
                ('unit_price', models.DecimalField(max_digits=6, default=0, decimal_places=2)),
                ('quantity', models.DecimalField(max_digits=12, default=0, decimal_places=4)),
                ('total_price', models.DecimalField(max_digits=12, default=0, decimal_places=2)),
            ],
            options={
                'db_table': 'notes_investments',
            },
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('modify_time', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50)),
                ('note_type', models.CharField(choices=[('1', '备忘录'), ('2', '投资'), ('3', '记账')], max_length=2)),
                ('begin_date', models.CharField(max_length=20)),
                ('end_date', models.CharField(max_length=20)),
                ('is_all_day', models.CharField(max_length=1)),
                ('user_id', models.CharField(default='ajay', max_length=30)),
                ('remark', models.TextField()),
            ],
            options={
                'db_table': 'notes',
            },
        ),
        migrations.AddField(
            model_name='invest_notes',
            name='note',
            field=models.ForeignKey(to='note.Notes'),
        ),
        migrations.AddField(
            model_name='account_notes',
            name='note',
            field=models.ForeignKey(to='note.Notes'),
        ),
    ]
