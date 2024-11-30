from django.urls import path

from catalog.apiview_controller import API_Catalog

router_catalog = [
    path('catalog', API_Catalog.as_view(), name='catalog')
]