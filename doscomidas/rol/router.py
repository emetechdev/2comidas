from django.urls import path

from rol.apiview_controller import API_Rol

router_rol = [
    path('rol', API_Rol.as_view(), name='rol')
]