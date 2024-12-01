from django.db import models

from user.models import User_Model
from order.models import Order_Model

class Delivery_Model(models.Model):
    """Delivery model."""
    pk_delivery = models.AutoField(primary_key=True)
    fk_user = models.ForeignKey(User_Model, on_delete=models.RESTRICT)
    fk_order = models.ForeignKey(Order_Model, on_delete=models.RESTRICT)
    
    order_number = models.CharField('Nro. Pedido', max_length=30)
    restaurant_name = models.CharField('Nombre restaurante', max_length=50)
    dish_name = models.CharField('Nombre plato', max_length=50)
    destination_location = models.CharField('Ubicacion destino', max_length=25)
    origin_location = models.CharField('Ubicacion origen', max_length=25)
    delivery_state = models.CharField('Estado entrega', max_length=20)
    comments = models.CharField('Comentarios', max_length=300)

class Meta:
    """Se usa para agregar metadatos extendidos"""
    verbose_name = 'envio'
    verbose_name_plural = 'envios'
