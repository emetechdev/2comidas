from django.db import models

#from ..usuario.models import User
#from ..order.models import Order

class Delivery_In_Place_Model(models.Model):
    """Delivery model."""
    pk_delivery_in_place = models.AutoField(primary_key=True)
    #fk_user = models.ForeignKey(User, on_delete=models.CASCADE)
    #fk_order = models.ForeignKey(Order, on_delete=models.CASCADE)
    
    order_number = models.CharField('Nro. Pedido', max_length=30)
    restaurant_name = models.CharField('Nombre restaurante', max_length=50)
    dish_name = models.CharField('Nombre plato', max_length=50)
    delivery_state = models.CharField('Estado entrega', max_length=20)
    comments = models.CharField('Comentarios', max_length=300)

class Meta:
    """Se usa para agregar metadatos extendidos"""
    verbose_name = 'entrega'
    verbose_name_plural = 'entregas'
