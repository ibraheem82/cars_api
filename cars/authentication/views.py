from re import I
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response 
# Create your views here.

class WelcomeAuthView(generics.GenericAPIView):
    def get(self, request):
        return Response(data={"Message": "Hello Auth"}, status=status.HTTP_200_OK)
        
