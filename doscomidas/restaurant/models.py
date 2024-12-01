from django.db import models

from location.models import Location_Model
from user.models import User_Model

class Restaurant_Model(models.Model):
    pk_restaurant= models.AutoField(primary_key=True)
    fk_location = models.ForeignKey(Location_Model, on_delete=models.RESTRICT)
    fk_responsible_user_id = models.ForeignKey(User_Model, on_delete=models.RESTRICT)

    cuit = models.CharField('CUIT', max_length=11)
    company_name = models.CharField('Razon social', max_length=50)
    

class Meta:
    """Se usa para agregar metadatos extendidos"""
    verbose_name = 'restaurante'
    verbose_name_plural = 'restaurantes'
