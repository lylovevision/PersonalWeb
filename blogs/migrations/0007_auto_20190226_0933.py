# Generated by Django 2.0.13 on 2019-02-26 01:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_auto_20190226_0916'),
    ]

    operations = [
        migrations.CreateModel(
            name='Labels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lable', models.CharField(max_length=7, verbose_name='标签名称')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.AlterField(
            model_name='blogs',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 26, 9, 33, 13, 237889), verbose_name='添加时间'),
        ),
        migrations.AddField(
            model_name='labels',
            name='blog_lables',
            field=models.ManyToManyField(to='blogs.Blogs'),
        ),
    ]
