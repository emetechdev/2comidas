from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from location.models import Location_Model
from location.serializer import (
    SaveLocation_Serializer,
    InquiryLocation_Serializer
    )
   
class API_Location(APIView):
    """Api ubicacion"""
    allowed_methods = ['GET', 'POST']

    def get(self, request):
        """Retorna una lista de ubicaciones"""
        model = Location_Model.objects.all()
        serializer =  InquiryLocation_Serializer(model, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """Guarda una ubicacion"""
        serializer =  SaveLocation_Serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
