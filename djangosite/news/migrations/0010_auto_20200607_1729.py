# Generated by Django 3.0.7 on 2020-06-07 14:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_auto_20200607_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 7, 17, 29, 22, 692819), verbose_name='Publication date'),
        ),
    ]
