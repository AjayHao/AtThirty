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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('modify_time', models.DateTimeField(auto_now=True)),
                ('commodity_name', models.CharField(max_length=50)),
                ('commodity_type', models.CharField(max_length=3)),
                ('direction', models.CharField(max_length=1)),
                ('total_price', models.DecimalField(max_digits=12, decimal_places=2)),
            ],
            options={
                'db_table': 'notes_accounts',
            },
        ),
        migrations.CreateModel(
            name='Invest_Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('modify_time', models.DateTimeField(auto_now=True)),
                ('security_name', models.CharField(max_length=50)),
                ('direction', models.CharField(max_length=1)),
                ('unit_price', models.DecimalField(max_digits=6, decimal_places=2, default=0)),
                ('quantity', models.DecimalField(max_digits=12, decimal_places=4, default=0)),
                ('total_price', models.DecimalField(max_digits=12, decimal_places=2, default=0)),
            ],
            options={
                'db_table': 'notes_investments',
            },
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('modify_time', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50)),
                ('note_type', models.CharField(max_length=2, choices=[('1', '备忘录'), ('2', '投资'), ('3', '记账')])),
                ('begin_date', models.CharField(max_length=20)),
                ('end_date', models.CharField(max_length=20)),
                ('is_all_day', models.CharField(max_length=1)),
                ('user_id', models.CharField(max_length=30, default='ajay')),
                ('remark', models.TextField()),
            ],
            options={
                'db_table': 'notes',
            },
        ),
        migrations.AddField(
            model_name='invest_notes',
            name='note',
            field=models.ForeignKey(to='blog.Notes'),
        ),
        migrations.AddField(
            model_name='account_notes',
            name='note',
            field=models.ForeignKey(to='blog.Notes'),
        ),
    ]
