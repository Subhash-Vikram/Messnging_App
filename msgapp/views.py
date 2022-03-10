from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
# from msgapp.database import auth_user, is_Admin, list_of_users
from msgapp.generic_functions import isValidJson
from msgapp.manage_user import add_user, update_user, delete_user, auth_user, is_Admin, list_of_users


# Create your views here.
# Login API for all users
class Login(APIView):
    def get(self, request):
        username = request.META.get('HTTP_USERNAME')
        password = request.META.get('HTTP_PASSWORD')
        status = auth_user(username, password)
        return JsonResponse(status)


# Admin API to view all the users
class Admin(APIView):
    def get(self, request):
        username = request.META.get('HTTP_USERNAME')
        if is_Admin(username):
            # json_val = request.body
            # if isValidJson(json_val) and (str(json_val.decode('utf-8')) != ''):
            return JsonResponse(list_of_users(), safe=False)
        else:
            return JsonResponse({"Status": "Failed",
                                 "Message": "Only Admin user can view this page"})


# Admin API to create new user
class Adduser(APIView):
    def post(self, request):
        username = request.META.get('HTTP_USERNAME')
        if is_Admin(username):
            json_val = request.body
            if isValidJson(json_val) and (str(json_val.decode('utf-8')) != ''):
                return JsonResponse(add_user(json_val))
            else:
                return JsonResponse({"Status": "Failed",
                                     "Message": "Please send the valid body to proceed"})
        else:
            return JsonResponse({"Status": "Failed",
                                 "Message": "Only Admin user can view this page"})


# Admin API to update an existing user
class Updateuser(APIView):
    def post(self, request):
        username = request.META.get('HTTP_USERNAME')
        if is_Admin(username):
            json_val = request.body
            if isValidJson(json_val) and (str(json_val.decode('utf-8')) != ''):
                return JsonResponse(update_user(json_val))
            else:
                return JsonResponse({"Status": "Failed",
                                     "Message": "Please send the valid body to proceed"})
        else:
            return JsonResponse({"Status": "Failed",
                                 "Message": "Only Admin user can view this page"})


# Admin API to delete an existing user
class Deleteuser(APIView):
    def post(self, request):
        username = request.META.get('HTTP_USERNAME')
        if is_Admin(username):
            json_val = request.body
            if isValidJson(json_val) and (str(json_val.decode('utf-8')) != ''):
                return JsonResponse(delete_user(json_val))
            else:
                return JsonResponse({"Status": "Failed",
                                     "Message": "Please send the valid body to proceed"})
        else:
            return JsonResponse({"Status": "Failed",
                                 "Message": "Only Admin user can view this page"})
