# Generated by Django 3.0.5 on 2020-04-12 12:06

from django.db import migrations, models
import musers.models


class Migration(migrations.Migration):

    dependencies = [
        ('musers', '0005_auto_20200408_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='muser',
            name='profile_photo',
            field=models.FileField(blank=True, null=True, upload_to=musers.models.upload_to_image),
        ),
    ]