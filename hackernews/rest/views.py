from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveUpdateDestroyAPIView , ListCreateAPIView , RetrieveAPIView , CreateAPIView , ListAPIView , RetrieveUpdateAPIView , RetrieveDestroyAPIView
from rest_framework.response import Response
from backend.models import Links , UserWithPhoto , Message
from .serlizer import LinksSerializer , UserWithPhotoSerializer , MessageSerializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.
class LinksViewset(ModelViewSet):
    queryset = Links.objects.all()
    serializer_class = LinksSerializer

class MessagesViewset(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class usersViewset(ModelViewSet):
    queryset = UserWithPhoto.objects.all()
    serializer_class = UserWithPhotoSerializer
#class ListApi(ListAPIView):
 #   def get_queryset(self):
  #      return Links.objects.all()
   # serializer_class = LinksSerializer

#class ListDetroy(RetrieveUpdateDestroyAPIView):
 #   queryset = Links
  #  serializer_class = LinksSerializer
   # lookup_field = 'slug'
    
#class Retrivelink(RetrieveAPIView):
 #   queryset = Links
  #  serializer_class = LinksSerializer
   # lookup_field = 'slug'

#class DeleteApi(RetrieveDestroyAPIView):
 #   queryset = Links
  #  serializer_class = LinksSerializer
   # lookup_field = 'slug'

#class CreateApi(ListCreateAPIView):
 #   def get_queryset(self):
  #      return Links.objects.all()
   # serializer_class = LinksSerializer

#class ListUser(ListAPIView):
 #   def get_queryset(self):
  #      return UserWithPhoto.objects.all()
   # serializer_class = UserWithPhotoSerializer

#class UserDetroy(RetrieveUpdateDestroyAPIView):
 #   queryset = UserWithPhoto
  #  serializer_class = UserWithPhotoSerializer
   # lookup_field = 'pk'
    
#class RetriveUser(RetrieveAPIView):
 #   queryset = UserWithPhoto
  #  serializer_class = UserWithPhotoSerializer
   # lookup_field = 'pk'

#class DeleteUser(RetrieveDestroyAPIView):
 #   queryset = UserWithPhoto
  #  serializer_class = UserWithPhotoSerializer
   # lookup_field = 'pk'

#class CreateUser(ListCreateAPIView):
 #   def get_queryset(self):
  #      return UserWithPhoto.objects.all()
   # serializer_class = UserWithPhotoSerializer