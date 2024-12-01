"""Serializer. Convierte la estructura del orm de django en una estructura JSON."""
from rest_framework import serializers

from order.models import Order_Model
from dish.serializer import InquiryDish_Serializer
from restaurant.serializer import InquiryRestaurant_Serializer

class SaveOrder_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Model
        # Campos disponibles para el insert (BD)
        fields = [
            "fk_dish",
            "fk_restaurant",

            "order_number",
            "dish_name",
            "quota_abailable",
            "qualification",
            "dispatch",
        ]

class InquiryOrder_Serializer(serializers.ModelSerializer):
    fk_dish = InquiryDish_Serializer(many=True, read_only=True)
    fk_restaurant = InquiryRestaurant_Serializer(read_only=True)

    class Meta:
        model = Order_Model
        fields = '__all__'

        