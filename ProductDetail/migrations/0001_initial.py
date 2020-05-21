# Generated by Django 2.2.4 on 2019-10-23 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='NA', max_length=200)),
                ('description', models.TextField(default='')),
                ('metrics', models.ManyToManyField(blank=True, related_name='product_metrics', to='ProductDetail.Metric')),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('catagory', models.TextField(default='')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='ProductDetail.Product')),
            ],
        ),
    ]