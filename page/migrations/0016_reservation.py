# Generated by Django 5.0.3 on 2024-04-21 08:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0015_alter_mapdata_latitude_alter_mapdata_longitude'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('time', models.TimeField(verbose_name='Время')),
                ('number_of_people', models.IntegerField(verbose_name='Количество людей')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Номер телефона')),
                ('additional_requests', models.TextField(blank=True, null=True, verbose_name='Особые пожелание')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.restaurant')),
            ],
        ),
    ]