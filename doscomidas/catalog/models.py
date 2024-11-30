from django.db import models

#from ..plato.models import Dish
#from ..restaurant.models import Restaurant

class Catalog_Model(models.Model):
    pk_catalog = models.AutoField(primary_key=True)
    #fk_dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    #fk_restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    restaurant_name = models.CharField('Nombre restaurante', max_length=50)
    dish_name = models.CharField('Nombre plato', max_length=50)
    

class Meta:
    """Se usa para agregar metadatos extendidos"""
    verbose_name = 'catalogo'
    verbose_name_plural = 'catalogos'
