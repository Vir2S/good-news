# Generated by Django 3.0.7 on 2020-06-09 08:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0023_auto_20200609_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 9, 11, 47, 53, 38684), verbose_name='Publication date'),
        ),
    ]
