# Generated by Django 3.0.7 on 2020-06-07 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20200607_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='short_story',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.CharField(max_length=160),
        ),
    ]
