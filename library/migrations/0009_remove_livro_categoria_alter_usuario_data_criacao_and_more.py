# Generated by Django 5.0.6 on 2024-06-23 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_alter_usuario_data_criacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livro',
            name='categoria',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='data_criacao',
            field=models.DateField(default='23/06/2024'),
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Livro',
        ),
    ]
