from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from catalog.models import Catalog_Model
from catalog.serializer import (
    SaveCatalog_Serializer,
    InquiryCatalog_Serializer
    )
   
class API_Catalog(APIView):
    """Api ubicacion"""
    allowed_methods = ['GET', 'POST']

    def get(self, request):
        """Retorna una lista de ubicaciones"""
        model = Catalog_Model.objects.all()
        serializer =  SaveCatalog_Serializer(model, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """Guarda una ubicacion"""
        serializer =  InquiryCatalog_Serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
