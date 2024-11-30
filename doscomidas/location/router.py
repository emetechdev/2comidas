from django.urls import path

from location.apiview_controller import API_Location

router_location = [
    path('location', API_Location.as_view(), name='ubicacion')
]