from django.urls import path

from delivery_in_place.apiview_controller import API_Delivery_In_Place

router_delivery_in_place = [
    path('delivery-in-place', API_Delivery_In_Place.as_view(), name='delivery-in-place')
]