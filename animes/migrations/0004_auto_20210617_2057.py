# Generated by Django 3.2.4 on 2021-06-17 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0003_anime_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='eps_assistidos',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='anime',
            name='n_eps',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='anime',
            name='nota',
            field=models.CharField(max_length=100),
        ),
    ]
