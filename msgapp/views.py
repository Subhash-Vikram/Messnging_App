from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class Login(APIView):
    def get(self, request):
        username = request.META.get('HTTP_USERNAME')
        password = request.META.get('HTTP_PASSWORD')

        return JsonResponse({"Status": "Login Successfully"})
