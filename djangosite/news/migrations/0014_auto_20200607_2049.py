# Generated by Django 3.0.7 on 2020-06-07 17:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_auto_20200607_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 7, 20, 49, 48, 292051), verbose_name='Publication date'),
        ),
    ]
