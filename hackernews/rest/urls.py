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
from .views import ListRud , ListApi , Retrivelink
urlpatterns = [
    path('' , include('rest_framework.urls')),
    path('list/' , ListApi.as_view() , name='list_links'),
    path('rud/<str:slug>' , ListRud.as_view() , name='list_rud'),
    path('link/<str:slug>' , Retrivelink.as_view() , name='link'),
    
]

