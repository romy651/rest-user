# Generated by Django 2.2.5 on 2020-03-17 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_auto_20200317_0653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='description',
            field=models.TextField(max_length=255),
        ),
    ]
