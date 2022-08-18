from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveUpdateDestroyAPIView , ListCreateAPIView , RetrieveAPIView , CreateAPIView , ListAPIView , RetrieveUpdateAPIView
from rest_framework.response import Response
from backend.models import Links , UserWithPhoto , Message
from .serlizer import LinksSerializer , UserWithPhotoSerializer , MessageSerializer
# Create your views here.
class ListApi(ListAPIView):
    def get_queryset(self):
        return Links.objects.all()
    serializer_class = LinksSerializer

class ListRud(RetrieveUpdateDestroyAPIView):
    queryset = Links
    serializer_class = LinksSerializer
    lookup_field = 'slug'

class Retrivelink(RetrieveAPIView):
    queryset = Links
    serializer_class = LinksSerializer
    lookup_field = 'slug'