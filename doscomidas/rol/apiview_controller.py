from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from rol.models import Rol_Model
from rol.serializer import (
    SaveRol_Serializer,
    InquiryRol_Serializer
    )
   
class API_Rol(APIView):
    """Api ubicacion"""
    allowed_methods = ['GET', 'POST']

    def get(self, request):
        """Retorna una lista de ubicaciones"""
        model = Rol_Model.objects.all()
        serializer =  InquiryRol_Serializer(model, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """Guarda una ubicacion"""
        serializer =  SaveRol_Serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
