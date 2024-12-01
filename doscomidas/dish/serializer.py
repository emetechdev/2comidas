"""Serializer. Convierte la estructura del orm de django en una estructura JSON."""
from rest_framework import serializers

from dish.models import Dish_Model

class SaveDish_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Dish_Model
        # Campos disponibles para el insert (BD)
        fields = [
            "fk_restaurant",

            "name",
            "calories",
            "description",
            "nutrition",
            "qualification",
        ]

class InquiryDish_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Dish_Model
        fields = '__all__'

        