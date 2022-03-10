"""Messnging_App URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from msgapp import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', views.default.as_view()),
    path('Login/', views.Login.as_view()),
    path('Admin/', views.Admin.as_view()),
    path('Admin/adduser/', views.Adduser.as_view()),
    path('Admin/updateuser/', views.Updateuser.as_view()),
    path('Admin/deleteuser/', views.Deleteuser.as_view()),
    path('Group/', views.Group.as_view()),
    path('Group/create', views.Creategroup.as_view()),
    path('Group/delete', views.Deletegroup.as_view()),
    path('Group/search', views.Searchgroup.as_view()),
    path('Group/addmembers', views.Addmembers.as_view()),
    path('Group/removemembers', views.Removemembers.as_view()),
    path('Group/Messages', views.Viewmessages.as_view()),
    path('Group/Sendmessage', views.Sendmessage.as_view()),
    path('Group/Likemessage', views.Likemessage.as_view()),
]
