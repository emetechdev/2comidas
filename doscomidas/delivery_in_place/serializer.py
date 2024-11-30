"""Serializer. Convierte la estructura del orm de django en una estructura JSON."""
from rest_framework import serializers

from delivery_in_place.models import Delivery_In_Place_Model

class SaveDelivery_In_Place_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery_In_Place_Model
        # Campos disponibles para el insert (BD)
        fields = [
            "order_number",
            "restaurant_name",
            "dish_name",
            "delivery_state",
            "comments",
        ]

class InquiryDelivery_In_Place_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery_In_Place_Model
        fields = '__all__'

        