from django.urls import path

from delivery_in_place.apiview_controller import API_User

router_delivery_in_place = [
    path('delivery-in-place', API_User.as_view(), name='delivery-in-place')
]