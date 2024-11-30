"""
URL configuration for doscomidas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from catalog.router import router_catalog
from credential.router import router_credential
from delivery_in_place.router import router_delivery_in_place
from delivery.router import router_delivery
from dish.router import router_dish
from location.router import router_location
from order.router import router_order
from restaurant.router import router_restaurant
from rol.router import router_rol
from user.router import router_user


urlpatterns = [
    path('admin/', admin.site.urls),

    # api urls
    path('api/', include(router_catalog)),
    path('api/', include(router_credential)),
    path('api/', include(router_delivery)),
    path('api/', include(router_delivery_in_place)),
    path('api/', include(router_dish)),
    path('api/', include(router_location)),
    path('api/', include(router_order)),
    path('api/', include(router_restaurant)),
    path('api/', include(router_rol)),
    path('api/', include(router_user)),
]
