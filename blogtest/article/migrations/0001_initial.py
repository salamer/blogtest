# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50)),
                ('data_time', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('editor', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('commentator', models.CharField(max_length=100)),
                ('comment', models.TextField(max_length=200)),
                ('data_time', models.DateTimeField(auto_now_add=True)),
                ('link', models.ForeignKey(to='article.Article')),
            ],
        ),
    ]
