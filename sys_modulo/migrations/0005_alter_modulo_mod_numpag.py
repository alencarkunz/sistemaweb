# Generated by Django 4.0.5 on 2022-06-25 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sys_modulo', '0004_modulo_mod_numpag_alter_modulo_mod_mdl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulo',
            name='MOD_NUMPAG',
            field=models.SmallIntegerField(default=25, null=True, verbose_name='Paginas'),
        ),
    ]
