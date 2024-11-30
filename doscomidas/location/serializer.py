"""Serializer. Convierte la estructura del orm de django en una estructura JSON."""
from rest_framework import serializers

from location.models import Location_Model

class SaveLocation_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Location_Model
        # Campos disponibles para el insert (BD)
        fields = [
            "name",
            "bulding",
            "street",
            "street_number",
            "neighborhood",
            "city",
            "province",
            "latitude",
            "longitude",
            "extra_references",
        ]

class InquiryLocation_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Location_Model
        fields = '__all__'

        