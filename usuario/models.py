from django.db import models

from ..ubicacion.models import Location
from ..rol.models import Rol
from ..credenciales.models import Credential

class User(models.Model):
    """User model."""
    pk_user = models.AutoField(primary_key=True)
    fk_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    fk_rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    fk_credential = models.ForeignKey(Credential, on_delete=models.CASCADE)
    
    names = models.CharField('Nombres', max_length=50)
    last_name = models.CharField('Apellidos', max_length=50)
    dni = models.CharField('DNI', max_length=8)
    birthdate = models.DateField(help_text='Fecha nacimiento')
    email = models.CharField('Email', max_length=50)

class Meta:
    """Se usa para agregar metadatos extendidos"""
    verbose_name = 'usuario'
    verbose_name_plural = 'usuarios'
