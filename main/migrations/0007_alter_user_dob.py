# Generated by Django 3.2.8 on 2021-10-29 10:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20211029_0345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='DOB',
            field=models.DateField(default=datetime.datetime(2021, 10, 29, 10, 59, 5, 754722, tzinfo=utc)),
        ),
    ]
