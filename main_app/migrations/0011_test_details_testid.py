# Generated by Django 2.0.2 on 2018-03-06 03:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_auto_20180304_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='test_details',
            name='testid',
            field=models.IntegerField(default=0000),
            preserve_default=False,
        ),
    ]
