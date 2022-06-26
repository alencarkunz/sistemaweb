# Generated by Django 4.0.5 on 2022-06-24 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sys_permissao', '0001_initial'),
        ('sys_usuario', '0003_usuario_per_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='PER_ID',
            field=models.ForeignKey(db_column='PER_ID', on_delete=django.db.models.deletion.PROTECT, to='sys_permissao.permissao', verbose_name='Permissão'),
        ),
    ]