# Generated by Django 3.0.7 on 2020-06-07 18:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_auto_20200607_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 7, 21, 16, 0, 276442), verbose_name='Publication date'),
        ),
        migrations.AlterField(
            model_name='article',
            name='full_story',
            field=models.TextField(),
        ),
    ]
