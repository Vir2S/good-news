# Generated by Django 3.0.7 on 2020-06-08 20:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0019_auto_20200608_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 8, 23, 1, 34, 103581), verbose_name='Publication date'),
        ),
    ]
