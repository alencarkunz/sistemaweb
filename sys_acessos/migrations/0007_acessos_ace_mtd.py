# Generated by Django 4.0.5 on 2022-07-18 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sys_acessos', '0006_alter_acessos_ace_dathor'),
    ]

    operations = [
        migrations.AddField(
            model_name='acessos',
            name='ACE_MTD',
            field=models.CharField(max_length=20, null=True, verbose_name='Method'),
        ),
    ]
