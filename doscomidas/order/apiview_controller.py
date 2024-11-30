from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from order.models import Order_Model
from order.serializer import (
    SaveOrder_Serializer,
    InquiryOrder_Serializer
    )
   
class API_Order(APIView):
    """Api ubicacion"""
    allowed_methods = ['GET', 'POST']

    def get(self, request):
        """Retorna una lista de ubicaciones"""
        model = Order_Model.objects.all()
        serializer =  InquiryOrder_Serializer(model, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """Guarda una ubicacion"""
        serializer =  SaveOrder_Serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
