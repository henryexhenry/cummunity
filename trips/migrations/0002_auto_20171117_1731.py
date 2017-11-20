# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 09:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='App_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.TextField()),
                ('post_pk', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]