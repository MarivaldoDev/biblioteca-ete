# Generated by Django 5.0.6 on 2024-05-26 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_remove_livro_quantidade_livro_data_devolucao_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='administrador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=20)),
                ('senha', models.CharField(max_length=8)),
            ],
        ),
        migrations.RenameModel(
            old_name='Perfil',
            new_name='Usuario',
        ),
    ]
