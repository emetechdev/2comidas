from django.urls import path

from dish.apiview_controller import API_Dish

router_dish = [
    path('dish', API_Dish.as_view(), name='dish')
]