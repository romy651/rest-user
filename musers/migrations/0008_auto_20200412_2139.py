# Generated by Django 3.0.5 on 2020-04-12 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musers', '0007_auto_20200412_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='muser',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
