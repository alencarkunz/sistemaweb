# Generated by Django 4.0.5 on 2022-07-01 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sys_acessos', '0002_rename_id_usuario_acessos_id_usu'),
    ]

    operations = [
        migrations.RenameField(
            model_name='acessos',
            old_name='ID_USU',
            new_name='id_usuario',
        ),
    ]
