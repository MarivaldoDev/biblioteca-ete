# Generated by Django 5.0.6 on 2024-06-23 17:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_remove_livro_categoria_alter_usuario_data_criacao_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=20)),
                ('senha', models.CharField(max_length=8)),
            ],
            options={
                'verbose_name_plural': 'administrators',
            },
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('livro', models.CharField(max_length=100)),
                ('categoria', models.CharField(blank=True, max_length=50)),
                ('data_emprestimo', models.DateField(default='23/06/2024')),
                ('data_devolucao', models.DateField(default='23/06/2024')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('matricula', models.CharField(max_length=7)),
                ('curso', models.CharField(max_length=40)),
                ('turma', models.CharField(max_length=10)),
                ('data_criacao', models.DateField(default='23/06/2024')),
                ('imagem', models.ImageField(blank=True, upload_to='imagem_cadastro/%Y/%m/')),
            ],
            options={
                'verbose_name_plural': 'users',
            },
        ),
        migrations.DeleteModel(
            name='administrador',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='portador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.user'),
        ),
    ]
