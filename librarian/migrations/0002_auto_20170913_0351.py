# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-12 22:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('o', 'On loan'), ('a', 'Available'), ('r', 'Reserved')], default='a', help_text='Book availability', max_length=1),
        ),
        migrations.AlterField(
            model_name='issuedata',
            name='due_back',
            field=models.DateField(blank=True, default=datetime.date(2017, 9, 28), null=True),
        ),
    ]
