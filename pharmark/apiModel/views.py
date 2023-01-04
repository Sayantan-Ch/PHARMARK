from django.shortcuts import render
from rest_framework import generics , status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Drug 
import simplejson as json
from .serializers import CreateDrugSerializers , DrugSerializers
# Create your views here.
class DrugView(generics.ListAPIView):
    queryset= Drug.objects.all()
    serializer_class = DrugSerializers


class CreateDrugView(APIView):
    
    serializer_class = CreateDrugSerializers

    def post(self,request,format=None):
        
        serializer =  self.serializer_class(data=request.data)
        if serializer.is_valid():
            suggestionCode=serializer.data.get('suggestionCode')
            drugCode=serializer.data.get('drugCode')
            Approved=serializer.data.get('Approved')
            names=serializer.data.get('names')
            drugSuggestion=Drug(drugCode=drugCode,Approved=Approved,names=names)
            drugSuggestion.save()
            return Response(DrugSerializers(drugSuggestion).data,status=status.HTTP_200_OK)
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
    

# APIView basically overides default methods

    


