# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('movie_title', models.CharField(max_length=50)),
                ('user_rating', models.IntegerField(max_length=2, blank=True)),
                ('critics_rating', models.IntegerField(max_length=2, blank=True)),
                ('running_time_minutes', models.IntegerField(max_length=5)),
                ('release_date', models.DateField()),
                ('movie_description', models.TextField(blank=True)),
            ],
        ),
    ]
