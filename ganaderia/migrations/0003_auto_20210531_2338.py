# Generated by Django 3.1.7 on 2021-06-01 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ganaderia', '0002_vacamadre_id_animal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venta',
            old_name='id_venta',
            new_name='id_producto',
        ),
    ]
