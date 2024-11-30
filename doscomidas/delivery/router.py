from django.urls import path

from delivery.apiview_controller import API_Delivery

router_delivery = [
    path('delivery', API_Delivery.as_view(), name='delivery')
]