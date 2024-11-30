from django.db import models

class Location_Model(models.Model):
    """Location model. """
    pk_location = models.AutoField(primary_key=True)
    
    name = models.CharField('Nombre ubicacion', max_length=30)
    bulding = models.CharField('Edificio (piso, dpto)', max_length=40)
    street = models.CharField('Calle', max_length=30)
    street_number = models.CharField('Numero casa', max_length=10)
    neighborhood = models.CharField('Barrio', max_length=40)
    city = models.CharField('Localidad', max_length=20)
    province = models.CharField('Provincia', max_length=20)
    latitude = models.CharField('Latitud', max_length=25)
    longitude = models.CharField('Longitud', max_length=25)
    extra_references = models.CharField('Referencias adicionales', max_length=100)

class Meta:
    """Se usa para agregar metadatos extendidos"""
    verbose_name = 'ubicacion'
    verbose_name_plural = 'ubicaciones'