# Generated by Django 3.2.4 on 2021-06-18 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0004_auto_20210617_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos/%d/%m/%Y/'),
        ),
    ]