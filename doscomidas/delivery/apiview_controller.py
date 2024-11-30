from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from delivery.models import Delivery_Model
from delivery.serializer import (
    SaveDelivery_Serializer,
    InquiryDelivery_Serializer
    )
   
class API_Delivery(APIView):
    """Api ubicacion"""
    allowed_methods = ['GET', 'POST']

    def get(self, request):
        """Retorna una lista de ubicaciones"""
        model = Delivery_Model.objects.all()
        serializer =  InquiryDelivery_Serializer(model, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """Guarda una ubicacion"""
        serializer =  SaveDelivery_Serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
