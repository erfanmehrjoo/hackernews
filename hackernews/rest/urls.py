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
from django.urls import path , include
from .views import ListDetroy , ListApi , Retrivelink , DeleteApi  , CreateApi , ListUser , UserDetroy , RetriveUser , DeleteUser , CreateUser
urlpatterns = [
    path('' , include('rest_framework.urls')),
    path('' , ListApi.as_view() , name='list_links'),
    path('update/<str:slug>' , ListDetroy.as_view() , name='link-update'),
    path('link/<str:slug>' , Retrivelink.as_view() , name='link-single-list'),
    path('delete/<str:slug>/' , DeleteApi.as_view() , name='link-delete'),
    path('create/' , CreateApi.as_view() , name='link-create'),
    path('users/' , ListUser.as_view() , name='list_users'),
    path('update/user/<str:pk>' , UserDetroy.as_view() , name='user-update'),
    path('user/<str:pk>' , RetriveUser.as_view() , name='user-single-list'),
    path('delete/user/<str:pk>/' , DeleteUser.as_view() , name='user-delete'),
    path('create/user/' , CreateUser.as_view() , name='user-create'),
]

