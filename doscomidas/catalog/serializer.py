"""Serializer. Convierte la estructura del orm de django en una estructura JSON."""
from rest_framework import serializers

from catalog.models import Catalog_Model
from restaurant.serializer import InquiryRestaurant_Serializer
from dish.serializer import InquiryDish_Serializer

class SaveCatalog_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog_Model
        # Campos disponibles para el insert (BD)
        fields = [
            "fk_restaurant",
            "fk_dish",

            "restaurant_name",
            "dish_name"
        ]

class InquiryCatalog_Serializer(serializers.ModelSerializer):
    fk_restaurant = InquiryRestaurant_Serializer(many=True, read_only=True)
    fk_dish = InquiryDish_Serializer(many=True, read_only=True)

    class Meta:
        model = Catalog_Model
        fields = '__all__'

        