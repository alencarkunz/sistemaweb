# Generated by Django 4.0.5 on 2022-06-29 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DashbordAtendimento',
            fields=[
                ('DAD_ID', models.AutoField(primary_key=True, serialize=False, verbose_name='Código')),
                ('DAD_NOM', models.CharField(max_length=100, verbose_name='Nome')),
                ('DAD_ORD', models.SmallIntegerField(null=True, verbose_name='Ordem')),
                ('DAD_STA', models.BooleanField(default=1, verbose_name='Status')),
            ],
            options={
                'db_table': 'dashbord_atendimento',
                'ordering': ['DAD_ORD'],
            },
        ),
    ]
