from django.db import models

from location.models import Location_Model
from rol.models import Rol_Model

class User_Model(models.Model):
    """User model."""
    pk_user = models.AutoField(primary_key=True)
    fk_location = models.ForeignKey(Location_Model, on_delete=models.RESTRICT)
    fk_rol = models.ForeignKey(Rol_Model, on_delete=models.RESTRICT)
    
    names = models.CharField('Nombres', max_length=50)
    last_name = models.CharField('Apellidos', max_length=50)
    # dni sin puntos
    dni = models.CharField('DNI', max_length=8)
    # Formato YYYY-MM-DD
    birthdate = models.DateField(help_text='Fecha nacimiento')
    email = models.CharField('Email', max_length=50)

class Meta:
    """Se usa para agregar metadatos extendidos"""
    verbose_name = 'usuario'
    verbose_name_plural = 'usuarios'
