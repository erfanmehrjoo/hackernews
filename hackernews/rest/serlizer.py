from rest_framework.serializers import ModelSerializer
from backend.models import Links , UserWithPhoto , Message

class LinksSerializer(ModelSerializer):
    class Meta:
        model = Links
        fields = '__all__'

class UserWithPhotoSerializer(ModelSerializer):
    class Meta:
        model = UserWithPhoto
        fields = '__all__'

class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'