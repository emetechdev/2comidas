"""Serializer. Convierte la estructura del orm de django en una estructura JSON."""
from rest_framework import serializers

from catalog.models import Catalog_Model

class SaveCatalog_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog_Model
        # Campos disponibles para el insert (BD)
        fields = [
            "restaurant_name",
            "dish_name"
        ]

class InquiryCatalog_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog_Model
        fields = '__all__'

        