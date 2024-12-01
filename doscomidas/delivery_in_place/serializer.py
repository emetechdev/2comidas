"""Serializer. Convierte la estructura del orm de django en una estructura JSON."""
from rest_framework import serializers

from delivery_in_place.models import Delivery_In_Place_Model
from user.serializer import InquiryUser_Serializer
from order.serializer import InquiryOrder_Serializer

class SaveDelivery_In_Place_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery_In_Place_Model
        # Campos disponibles para el insert (BD)
        fields = [
            "fk_user",
            "fk_order",

            "order_number",
            "restaurant_name",
            "dish_name",
            "delivery_state",
            "comments",
        ]

class InquiryDelivery_In_Place_Serializer(serializers.ModelSerializer):
    fk_user = InquiryUser_Serializer(read_only=True)
    fk_order = InquiryOrder_Serializer(read_only=True)

    class Meta:
        model = Delivery_In_Place_Model
        fields = '__all__'

        