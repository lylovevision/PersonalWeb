# Generated by Django 2.0.13 on 2019-02-26 07:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0013_auto_20190226_1502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorys',
            name='add_time',
        ),
        migrations.AlterField(
            model_name='blogs',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 26, 15, 4, 57, 130298), verbose_name='添加时间'),
        ),
    ]
