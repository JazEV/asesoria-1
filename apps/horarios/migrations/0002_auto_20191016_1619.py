# Generated by Django 2.2.1 on 2019-10-16 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horarios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turno',
            name='codigo',
        ),
        migrations.AddField(
            model_name='turno',
            name='apellido',
            field=models.CharField(default='kalk', help_text='Ingrese el apellido.', max_length=40),
            preserve_default=False,
        ),
    ]