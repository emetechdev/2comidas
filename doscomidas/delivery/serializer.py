"""Serializer. Convierte la estructura del orm de django en una estructura JSON."""
from rest_framework import serializers

from delivery.models import Delivery_Model

class SaveDelivery_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery_Model
        # Campos disponibles para el insert (BD)
        fields = [
            "order_number",
            "restaurant_name",
            "dish_name",
            "destination_location",
            "origin_location",
            "delivery_state",
            "comments",
        ]

class InquiryDelivery_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery_Model
        fields = '__all__'

        