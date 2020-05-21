# Generated by Django 2.2.5 on 2020-03-17 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Muser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('surname', models.TextField()),
                ('birthdate', models.DateTimeField()),
                ('citezenship', models.TextField()),
                ('fname', models.TextField()),
                ('mname', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('profile_photo', models.TextField()),
                ('passport_number', models.TextField()),
                ('password', models.TextField()),
            ],
        ),
    ]