"""Serializer. Convierte la estructura del orm de django en una estructura JSON."""
from rest_framework import serializers

from order.models import Order_Model

class SaveOrder_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Model
        # Campos disponibles para el insert (BD)
        fields = [
            "order_number",
            "dish_name",
            "quota_abailable",
            "qualification",
            "dispatch",
        ]

class InquiryOrder_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Model
        fields = '__all__'

        