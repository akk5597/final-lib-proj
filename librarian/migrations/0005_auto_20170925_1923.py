# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-25 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0004_auto_20170925_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_Div',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], default='A', help_text='Div of student', max_length=1),
        ),
        migrations.AddField(
            model_name='student',
            name='student_class',
            field=models.CharField(choices=[('S', 'SE'), ('T', 'TE'), ('B', 'BE')], default='S', help_text='Class of student', max_length=1),
        ),
    ]
