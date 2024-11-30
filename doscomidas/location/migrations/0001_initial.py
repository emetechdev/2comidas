# Generated by Django 5.1.3 on 2024-11-30 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location_Model',
            fields=[
                ('pk_location', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, verbose_name='Nombre ubicacion')),
                ('bulding', models.CharField(max_length=40, verbose_name='Edificio (piso, dpto)')),
                ('street', models.CharField(max_length=30, verbose_name='Calle')),
                ('street_number', models.CharField(max_length=10, verbose_name='Numero casa')),
                ('neighborhood', models.CharField(max_length=40, verbose_name='Barrio')),
                ('city', models.CharField(max_length=20, verbose_name='Localidad')),
                ('province', models.CharField(max_length=20, verbose_name='Provincia')),
                ('latitude', models.CharField(max_length=25, verbose_name='Latitud')),
                ('longitude', models.CharField(max_length=25, verbose_name='Longitud')),
                ('extra_references', models.CharField(max_length=100, verbose_name='Referencias adicionales')),
            ],
        ),
    ]