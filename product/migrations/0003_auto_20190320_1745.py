# Generated by Django 2.1.7 on 2019-03-20 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20190320_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='start_time',
            field=models.FloatField(default=1553103911.6132858),
        ),
    ]
