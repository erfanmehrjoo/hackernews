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
from .views import LinksViewset , usersViewset , MessagesViewset
from rest_framework import routers
router = routers.SimpleRouter()
router.register('users' , usersViewset , basename='users')
router.register('links' , LinksViewset , basename='links')
router.register('messages' , MessagesViewset , basename='messages')
urlpatterns = [
    #path('' , include('rest_framework.urls')),
    path('' , include(router.urls)),
    path('rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

]

