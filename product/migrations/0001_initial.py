# Generated by Django 2.1.7 on 2019-03-19 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('howlong', models.SmallIntegerField()),
                ('howmany', models.SmallIntegerField()),
                ('start_time', models.FloatField(default=1553025136.3508625)),
                ('end_time', models.FloatField()),
                ('used', models.SmallIntegerField(default=0)),
                ('left', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('amazon_url', models.URLField(max_length=350)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=3, max_digits=15)),
                ('coupon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Coupon')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('small_picture', models.URLField(max_length=350)),
                ('large_picture', models.URLField(max_length=350)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='pictures',
            field=models.ManyToManyField(to='product.ProductPicture'),
        ),
    ]
