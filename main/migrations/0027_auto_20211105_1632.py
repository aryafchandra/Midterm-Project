# Generated by Django 3.2.7 on 2021-11-05 16:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_merge_0025_auto_20211105_1421_0025_auto_20211105_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagemodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 5, 16, 32, 50, 450948, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='DOB',
            field=models.DateField(default=datetime.datetime(2021, 11, 5, 16, 32, 50, 449830, tzinfo=utc)),
        ),
    ]
