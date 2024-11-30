from django.db import models

class Dish_Model(models.Model):
    pk_dish = models.AutoField(primary_key=True)
    
    name = models.CharField('Nombre', max_length=30)
    calories = models.CharField('Calorias', max_length=15)
    description = models.CharField('Descripcion', max_length=300)
    nutrition = models.CharField('Nutricion', max_length=300)
    qualification = models.IntegerField(help_text='Calificacion')

class Meta:
    """Se usa para agregar metadatos extendidos"""
    verbose_name = 'plato'
    verbose_name_plural = 'platos'