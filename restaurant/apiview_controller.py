from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from user.models import User_Model
from user.serializer import (
    SaveUser_Serializer,
    InquiryUser_Serializer
    )
   
class API_User(APIView):
    """Api ubicacion"""
    allowed_methods = ['GET', 'POST']

    def get(self, request):
        """Retorna una lista de ubicaciones"""
        model = User_Model.objects.all()
        serializer =  InquiryUser_Serializer(model, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """Guarda una ubicacion"""
        serializer =  SaveUser_Serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
