# Generated by Django 3.2.9 on 2021-11-05 12:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20211105_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagemodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 5, 12, 17, 35, 829635, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='DOB',
            field=models.DateField(default=datetime.datetime(2021, 11, 5, 12, 17, 35, 827605, tzinfo=utc)),
        ),
    ]
