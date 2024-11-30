from django.db import models

#from ..dish.models import Dish
#from ..restaurant.models import Restaurant

class Order_Model(models.Model):
    pk_order = models.AutoField(primary_key=True)
    #fk_dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    #fk_restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    order_number = models.CharField('Nro. Pedido', max_length=30)
    dish_name = models.CharField('Razon social', max_length=50)
    quota_abailable = models.IntegerField(help_text='Cupo disponible')
    qualification = models.IntegerField(help_text='Calificacion')
    dispatch = models.CharField('Despacho (envio/entrega)', max_length=100)
    

class Meta:
    """Se usa para agregar metadatos extendidos"""
    verbose_name = 'orden'
    verbose_name_plural = 'ordenes'
