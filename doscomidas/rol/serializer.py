"""Serializer. Convierte la estructura del orm de django en una estructura JSON."""
from rest_framework import serializers

from rol.models import Rol_Model

class SaveRol_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Rol_Model
        # Campos disponibles para el insert (BD)
        fields = [
            "name",
            "category"
        ]

class InquiryRol_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Rol_Model
        fields = '__all__'

        