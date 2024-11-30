from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from dish.models import Dish_Model
from dish.serializer import (
    SaveDish_Serializer,
    InquiryDish_Serializer
    )
   
class API_Dish(APIView):
    """Api ubicacion"""
    allowed_methods = ['GET', 'POST']

    def get(self, request):
        """Retorna una lista de ubicaciones"""
        model = Dish_Model.objects.all()
        serializer =  InquiryDish_Serializer(model, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """Guarda una ubicacion"""
        serializer =  SaveDish_Serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
