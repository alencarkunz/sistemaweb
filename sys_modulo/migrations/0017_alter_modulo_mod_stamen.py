# Generated by Django 4.0.5 on 2022-07-01 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sys_modulo', '0016_alter_modulo_mod_mdl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulo',
            name='MOD_STAMEN',
            field=models.BooleanField(default=1, verbose_name='Status Menu'),
        ),
    ]