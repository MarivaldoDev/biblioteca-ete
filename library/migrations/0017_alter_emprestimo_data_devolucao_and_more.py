# Generated by Django 5.0.6 on 2024-12-29 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0016_alter_emprestimo_data_devolucao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='data_devolucao',
            field=models.DateField(default='29/12/2024'),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='data_emprestimo',
            field=models.DateField(default='29/12/2024'),
        ),
    ]
