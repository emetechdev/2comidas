from django.db import models

class Rol_Model(models.Model):
    pk_rol = models.AutoField(primary_key=True)
    
    name = models.CharField('Nombre rol', max_length=30)
    category = models.CharField('Categoria', max_length=30)

class Meta:
    """Se usa para agregar metadatos extendidos"""
    verbose_name = 'rol'
    verbose_name_plural = 'roles'