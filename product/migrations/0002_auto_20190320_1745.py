# Generated by Django 2.1.7 on 2019-03-20 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='start_time',
            field=models.FloatField(default=1553103910.1748784),
        ),
    ]