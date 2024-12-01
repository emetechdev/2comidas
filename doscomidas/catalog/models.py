from django.db import models

from restaurant.models import Restaurant_Model
from dish.models import Dish_Model

class Catalog_Model(models.Model):
    """Catalog. Tabla intermedia. Realacoin M:N entre Restaurant y Dish."""
    pk_catalog = models.AutoField(primary_key=True)
    fk_restaurant = models.ForeignKey(Restaurant_Model, on_delete=models.CASCADE)
    fk_dish = models.ForeignKey(Dish_Model, on_delete=models.CASCADE)

    restaurant_name = models.CharField('Nombre restaurante', max_length=50)
    dish_name = models.CharField('Nombre plato', max_length=50)
    

class Meta:
    """Se usa para agregar metadatos extendidos"""
    verbose_name = 'catalogo'
    verbose_name_plural = 'catalogos'
