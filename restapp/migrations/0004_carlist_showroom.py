# Generated by Django 4.2.11 on 2024-05-17 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0003_showroomlist_alter_carlist_chassisnumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='carlist',
            name='showroom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='showrooms', to='restapp.showroomlist'),
        ),
    ]
