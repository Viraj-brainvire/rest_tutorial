# Generated by Django 4.2.11 on 2024-05-23 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0006_review_apiuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='carlist',
            name='passby',
            field=models.CharField(default='viraj_chauhan', max_length=80),
        ),
    ]
