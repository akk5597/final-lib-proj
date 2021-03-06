# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-11 16:31
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.CharField(help_text='Unique ID for this particular book across whole library', max_length=50, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200, null=True)),
                ('publisher', models.CharField(max_length=200, null=True)),
                ('status', models.CharField(choices=[('d', 'Maintenance'), ('o', 'On loan'), ('a', 'Available'), ('r', 'Reserved')], default='a', help_text='Book availability', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='IssueData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('due_back', models.DateField(blank=True, default=datetime.date(2017, 9, 26), null=True)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='librarian.Book')),
            ],
            options={
                'ordering': ['due_back'],
                'permissions': (('can_mark_returned', 'Set book as returned'),),
            },
        ),
        migrations.CreateModel(
            name='Librarian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('librarian_name', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=50)),
                ('student_id', models.CharField(max_length=14)),
                ('student_email', models.EmailField(max_length=254)),
                ('student_phno', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='issuedata',
            name='borrower',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='librarian.Student'),
        ),
    ]
