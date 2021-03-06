# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 09:50
from __future__ import unicode_literals

import blogs.models
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
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('content', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('viewedCount', models.IntegerField(default=0, editable=False)),
                ('coverimg', models.ImageField(blank=True, null=True, upload_to=blogs.models.upload_location)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('readtime', models.TimeField(blank=True, null=True)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
    ]
