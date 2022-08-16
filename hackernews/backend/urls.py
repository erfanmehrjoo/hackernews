"""hackernews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from cmath import nan
from django.contrib import admin
from django.urls import path
from .views import login_custom , logout_custom , register_custom , changepassword_custom , create_link , list_link , update_list

urlpatterns = [
    path('login/' , login_custom , name='login'),
    path('logout/' , logout_custom , name='logout'),
    path('register/' , register_custom , name='register'),
    path("changepassword/" , changepassword_custom , name='changepassword'),
    path('create/'  , create_link , name='create'), 
    path('list/' , list_link , name='list' ),
    path('update/<str:slug>' , update_list , name='update-list' ),
]
