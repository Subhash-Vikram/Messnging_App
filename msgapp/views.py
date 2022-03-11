# from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
# from rest_framework.response import Response
# from msgapp.database import auth_user, is_Admin, list_of_users
from msgapp.generic_functions import isValidJson
from msgapp.manage_user import add_user, update_user, delete_user, auth_user, is_Admin, list_of_users
from msgapp.manage_groups import list_of_groups


# Create your views here.
# Login API for all users
class Login(APIView):
    @staticmethod
    def get(request):
        username = request.META.get('HTTP_USERNAME')
        password = request.META.get('HTTP_PASSWORD')
        status = auth_user(username, password)
        return JsonResponse(status)


# Admin API to view all the users
class Admin(APIView):
    @staticmethod
    def get(request):
        username = request.META.get('HTTP_USERNAME')
        if is_Admin(username):
            return JsonResponse(list_of_users(), safe=False)
        else:
            return JsonResponse({"Status": "Failed",
                                 "Message": "Only Admin user can view this page"})


# Admin API to create new user
class Adduser(APIView):
    @staticmethod
    def post(request):
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
    @staticmethod
    def post(request):
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
    @staticmethod
    def post(request):
        username = request.META.get('HTTP_USERNAME')
        if is_Admin(username):
            json_val = request.body
            if isValidJson(json_val) and (str(json_val.decode('utf-8')) != ''):
                return JsonResponse(delete_user(json_val))
            else:
                return JsonResponse({"Status": "Failed",
                                     "Message": "Please send the valid body to proceed."})
        else:
            return JsonResponse({"Status": "Failed",
                                 "Message": "Only Admin user can view this page."})


# Group API which returns all Groups of current user
class Group(APIView):
    @staticmethod
    def get(request):
        username = request.META.get('HTTP_USERNAME')
        try:
            return JsonResponse(list_of_groups(username), safe=False)
        except Exception:
            return JsonResponse({"Status": "Failed",
                                 "Message": "Error occurred while accessing the groups."})
        pass
    pass


# API to create a new group
class Creategroup(APIView):
    pass


# API to delete group
class Deletegroup(APIView):
    pass


# API to search for a group
class Searchgroup(APIView):
    pass


# API to add members to group
class Addmembers(APIView):
    pass


# API to remove members from group
class Removemembers(APIView):
    pass


# API to view messages of given group
class Viewmessages(APIView):
    pass


# API to Send message in a group
class Sendmessage(APIView):
    pass


# API to Like a message of the group
class Likemessage(APIView):
    pass
