# Generated by Django 3.2.9 on 2021-11-05 11:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20211105_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagemodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 5, 11, 57, 32, 532820, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='DOB',
            field=models.DateField(default=datetime.datetime(2021, 11, 5, 11, 57, 32, 531795, tzinfo=utc)),
        ),
    ]