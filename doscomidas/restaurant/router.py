from django.urls import path

from restaurant.apiview_controller import API_Restaurant

router_restaurant = [
    path('restaurant', API_Restaurant.as_view(), name='restaurant')
]