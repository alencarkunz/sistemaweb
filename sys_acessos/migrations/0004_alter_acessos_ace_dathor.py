# Generated by Django 4.0.5 on 2022-07-01 07:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sys_acessos', '0003_rename_id_usu_acessos_id_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acessos',
            name='ACE_DATHOR',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 1, 7, 11, 8, 294710, tzinfo=utc), verbose_name='Data e Hora'),
        ),
    ]