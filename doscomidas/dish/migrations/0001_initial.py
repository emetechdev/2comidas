# Generated by Django 5.1.3 on 2024-12-01 01:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish_Model',
            fields=[
                ('pk_dish', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, verbose_name='Nombre')),
                ('calories', models.CharField(max_length=15, verbose_name='Calorias')),
                ('description', models.CharField(max_length=300, verbose_name='Descripcion')),
                ('nutrition', models.CharField(max_length=300, verbose_name='Nutricion')),
                ('qualification', models.IntegerField(help_text='Calificacion')),
                ('fk_restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.restaurant_model')),
            ],
        ),
    ]
