from django.db import models



class Credential(models.Model):
    pk_credential = models.AutoField(primary_key=True)
    
    dni = models.CharField('DNI', max_length=8)
    email = models.CharField('Email', max_length=30)
    password = models.CharField('Password', max_length=200)

class Meta:
    """Se usa para agregar metadatos extendidos"""
    verbose_name = 'credencial'
    verbose_name_plural = 'credenciales'