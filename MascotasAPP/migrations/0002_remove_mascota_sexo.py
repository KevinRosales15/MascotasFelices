# Generated by Django 5.0.4 on 2024-04-20 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MascotasAPP', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mascota',
            name='Sexo',
        ),
    ]