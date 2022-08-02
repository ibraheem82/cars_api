from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.response import Response 
# Create your views here.

class WelcomeOrderView(generics.GenericAPIView):
    def get(self, request):
        return Response(data={"Message": "Welcome orders api"}, status = status.HTTP_200_OK)