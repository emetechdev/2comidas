"""Serializer. Convierte la estructura del orm de django en una estructura JSON."""
from rest_framework import serializers

from user.models import User_Model
from location.serializer import InquiryLocation_Serializer
from rol.serializer import InquiryRol_Serializer


class SaveUser_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User_Model
        # Campos disponibles para el insert (BD)
        fields = [
            "fk_location",
            "fk_rol",

            "names",
            "last_name",
            "dni",
            "birthdate",
            "email",
        ]

class InquiryUser_Serializer(serializers.ModelSerializer):
 
    fk_location = InquiryLocation_Serializer(read_only=True)
    fk_rol = InquiryRol_Serializer(read_only=True)

    class Meta:
        model = User_Model
        fields = '__all__'

        