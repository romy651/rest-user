# Generated by Django 3.0.5 on 2020-04-14 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musers', '0010_auto_20200412_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='muser',
            name='accountId',
            field=models.TextField(default=452222),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Beneficiary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('surname', models.TextField()),
                ('birthdate', models.DateField()),
                ('citezenship', models.TextField()),
                ('passport_number', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musers.Muser')),
            ],
        ),
    ]
