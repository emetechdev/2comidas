"""Serializer. Convierte la estructura del orm de django en una estructura JSON."""
from rest_framework import serializers

from restaurant.models import Restaurant_Model
from location.serializer import InquiryLocation_Serializer
from user.serializer import InquiryUser_Serializer

class SaveRestaurant_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant_Model
        # Campos disponibles para el insert (BD)
        fields = [
            "fk_location",
            "fk_responsible_user_id",

            "cuit",
            "company_name",
        ]

class InquiryRestaurant_Serializer(serializers.ModelSerializer):
    fk_location = InquiryLocation_Serializer(read_only=True)
    # fix = hacer un serializer aparte para user porque esta
    # trayendo la ubicacion y el rol del usuario
    fk_responsible_user_id = InquiryUser_Serializer(read_only=True)

    class Meta:
        model = Restaurant_Model
        fields = '__all__'

        