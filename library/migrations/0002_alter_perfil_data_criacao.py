# Generated by Django 5.0.6 on 2024-05-25 17:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='data_criacao',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
