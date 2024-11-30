from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from delivery_in_place.models import Delivery_In_Place_Model
from delivery_in_place.serializer import (
    SaveDelivery_In_Place_Serializer,
    InquiryDelivery_In_Place_Serializer
    )
   
class API_Delivery_In_Place(APIView):
    """Api ubicacion"""
    allowed_methods = ['GET', 'POST']

    def get(self, request):
        """Retorna una lista de ubicaciones"""
        model = Delivery_In_Place_Model.objects.all()
        serializer =  InquiryDelivery_In_Place_Serializer(model, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """Guarda una ubicacion"""
        serializer =  SaveDelivery_In_Place_Serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
