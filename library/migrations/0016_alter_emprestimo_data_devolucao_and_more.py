# Generated by Django 5.0.6 on 2024-12-27 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0015_rename_user_userstandard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='data_devolucao',
            field=models.DateField(default='27/12/2024'),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='data_emprestimo',
            field=models.DateField(default='27/12/2024'),
        ),
    ]