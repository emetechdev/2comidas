"""Serializer. Convierte la estructura del orm de django en una estructura JSON."""
from rest_framework import serializers

from restaurant.models import Restaurant_Model

class SaveRestaurant_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant_Model
        # Campos disponibles para el insert (BD)
        fields = [
            "cuit",
            "company_name",
        ]

class InquiryRestaurant_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant_Model
        fields = '__all__'

        