"""Serializer. Convierte la estructura del orm de django en una estructura JSON."""
from rest_framework import serializers

from user.models import User_Model

class SaveUser_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User_Model
        # Campos disponibles para el insert (BD)
        fields = [
            "names",
            "last_name",
            "dni",
            "birthdate",
            "email",
        ]

class InquiryUser_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User_Model
        fields = '__all__'

        