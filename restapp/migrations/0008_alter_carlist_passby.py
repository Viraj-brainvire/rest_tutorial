# Generated by Django 4.2.11 on 2024-05-23 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0007_carlist_passby'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carlist',
            name='passby',
            field=models.CharField(max_length=80),
        ),
    ]
