# Generated by Django 2.2.1 on 2019-10-21 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novedades', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novedad',
            name='imagen',
            field=models.ImageField(blank=True, help_text='Opcional', null=True, upload_to='asesoria/novedades'),
        ),
    ]
