# Generated by Django 4.0.5 on 2022-06-26 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sys_usuario', '0002_alter_usuario_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='group_id',
            field=models.IntegerField(default=1, verbose_name='Permissão'),
            preserve_default=False,
        ),
    ]