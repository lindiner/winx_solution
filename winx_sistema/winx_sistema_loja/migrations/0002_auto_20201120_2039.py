# Generated by Django 3.1.3 on 2020-11-20 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winx_sistema_loja', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='idade',
            field=models.IntegerField(),
        ),
    ]
