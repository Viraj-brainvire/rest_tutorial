# Generated by Django 4.2.11 on 2024-05-17 06:37

from django.db import migrations, models
import restapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0002_carlist_chassisnumber_carlist_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='showRoomList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=100)),
                ('website', models.URLField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='carlist',
            name='chassisnumber',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[restapp.models.alphanumeric]),
        ),
    ]
