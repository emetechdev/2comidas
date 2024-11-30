from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from credential.models import Credential_Model
from credential.serializer import (
    SaveCredential_Serializer,
    InquiryCredential_Serializer
    )
   
class API_Credential(APIView):
    """Api ubicacion"""
    allowed_methods = ['GET', 'POST']

    def get(self, request):
        """Retorna una lista de ubicaciones"""
        model = Credential_Model.objects.all()
        serializer =  InquiryCredential_Serializer(model, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """Guarda una ubicacion"""
        serializer =  SaveCredential_Serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
