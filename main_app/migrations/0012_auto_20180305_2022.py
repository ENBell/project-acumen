# Generated by Django 2.0.2 on 2018-03-06 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_test_details_testid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test_details',
            name='num_variations',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='test_details',
            name='testid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='variation',
            name='varid',
            field=models.IntegerField(verbose_name=0),
        ),
    ]