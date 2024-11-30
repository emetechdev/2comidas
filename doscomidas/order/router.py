from django.urls import path

from order.apiview_controller import API_Order

router_order = [
    path('order', API_Order.as_view(), name='order')
]