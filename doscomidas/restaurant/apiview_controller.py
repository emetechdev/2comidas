from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from restaurant.models import Restaurant_Model
from restaurant.serializer import (
    SaveRestaurant_Serializer,
    InquiryRestaurant_Serializer
    )
   
class API_Restaurant(APIView):
    """Api ubicacion"""
    allowed_methods = ['GET', 'POST']

    def get(self, request):
        """Retorna una lista de ubicaciones"""
        model = Restaurant_Model.objects.all()
        serializer =  InquiryRestaurant_Serializer(model, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """Guarda una ubicacion"""
        serializer =  SaveRestaurant_Serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
