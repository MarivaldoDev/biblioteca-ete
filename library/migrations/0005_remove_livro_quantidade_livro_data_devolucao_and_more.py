# Generated by Django 5.0.6 on 2024-05-26 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_categoria_alter_perfil_curso_livro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livro',
            name='quantidade',
        ),
        migrations.AddField(
            model_name='livro',
            name='data_devolucao',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='livro',
            name='data_emprestimo',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='data_criacao',
            field=models.DateField(default='26/05/2024'),
        ),
    ]
