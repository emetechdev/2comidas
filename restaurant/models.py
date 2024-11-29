from django.db import models

from ..ubicacion.models import Location

class Restaurant(models.Model):
    pk_restaurant= models.AutoField(primary_key=True)
    fk_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    #fk_responsible_user_id = models.ForeignKey(Dish, on_delete=models.CASCADE)

    cuit = models.CharField('CUIT', max_length=11)
    company_name = models.CharField('Razon social', max_length=50)
    

class Meta:
    """Se usa para agregar metadatos extendidos"""
    verbose_name = 'restaurante'
    verbose_name_plural = 'restaurantes'
