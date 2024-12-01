"""Serializer. Convierte la estructura del orm de django en una estructura JSON."""
from rest_framework import serializers

from credential.models import Credential_Model

class SaveCredential_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Credential_Model
        # Campos disponibles para el insert (BD)
        fields = [
            "fk_user",

            "dni",
            "email",
            "password",
        ]

class InquiryCredential_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Credential_Model
        fields = '__all__'

        