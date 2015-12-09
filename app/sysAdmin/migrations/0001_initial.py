# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sche',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=8)),
                ('begindate', models.CharField(max_length=20)),
                ('enddate', models.CharField(max_length=20)),
                ('allday', models.CharField(max_length=1)),
                ('userid', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'sche_test',
            },
        ),
    ]
