# Generated by Django 5.0.3 on 2024-04-17 23:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0010_category_menu_dish_menu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish_menu',
            name='category',
        ),
        migrations.CreateModel(
            name='CategoryMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название Категории')),
                ('restaurant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='page.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='DishMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название Блюда')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('ingredients', models.TextField(verbose_name='Состав')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Цена')),
                ('image', models.ImageField(upload_to='Menu/', verbose_name='Фото')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.categorymenu')),
            ],
        ),
        migrations.DeleteModel(
            name='Category_menu',
        ),
        migrations.DeleteModel(
            name='dish_menu',
        ),
    ]
