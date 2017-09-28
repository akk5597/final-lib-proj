# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 04:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0007_auto_20170925_2034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('document', models.FileField(upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='issuedata',
            name='due_back',
            field=models.DateField(blank=True, default=datetime.date(2017, 10, 11), null=True),
        ),
    ]