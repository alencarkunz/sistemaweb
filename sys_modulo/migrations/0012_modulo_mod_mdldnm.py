# Generated by Django 4.0.5 on 2022-06-30 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sys_modulo', '0011_alter_modulo_mod_mdl'),
    ]

    operations = [
        migrations.AddField(
            model_name='modulo',
            name='MOD_MDLDNM',
            field=models.CharField(max_length=100, null=True, verbose_name='Modelo Dinâmico'),
        ),
    ]
