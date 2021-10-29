# Generated by Django 3.2.7 on 2021-10-29 03:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_messagemodel_threadmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='DOB',
            field=models.DateField(default=datetime.datetime(2021, 10, 29, 3, 45, 54, 122723, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='domicile',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='fullname',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='instagram',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='interest',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='line',
            field=models.CharField(default='', max_length=32),
        ),
    ]
